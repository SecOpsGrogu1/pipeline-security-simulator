# =============================
# Cloud Security Scanner - main.py
# Author: Paul M (SecOpsGrogu1)
#
# This script is a single-file, demo-friendly cloud security scanner for CI/CD pipelines.
# It detects mock vulnerabilities, supports auto-remediation, and provides clear results for DevSecOps workflows.
# =============================

import os  # For directory and file operations
import argparse  # For command-line argument parsing
import sys  # For system exit codes and script info

# --- Rules ---
# Here I define the mock security rules that the scanner will look for.
# Each rule has a name, a pattern to search for, a description, a severity level, and a remediation function.
MOCK_RULES = [
    {
        'name': 'Hardcoded Secret',  # Rule name
        'pattern': 'SECRET_KEY=',    # What to search for in files
        'desc': 'Possible hardcoded secret detected.',  # Description for output
        'severity': 'medium',  # How severe this finding is
        # Remediation: replace the secret with a redacted placeholder
        'remediate': lambda content: content.replace('SECRET_KEY=', 'SECRET_KEY="REDACTED_AUTO_REMEDIATED" # ')
    },
    {
        'name': 'Insecure Function',
        'pattern': 'eval(',
        'desc': 'Use of insecure eval() function.',
        'severity': 'high',  # This is high severity, since eval is dangerous
        # Remediation: comment out the eval usage
        'remediate': lambda content: content.replace('eval(', '# eval(  # AUTO-REMEDIATED: removed insecure eval')
    },
    {
        'name': 'Weak Hash',
        'pattern': 'md5(',
        'desc': 'Use of weak hash function md5.',
        'severity': 'low',  # Weak hash is less severe, but still not recommended
        # Remediation: replace md5 with sha256 and add a comment
        'remediate': lambda content: content.replace('md5(', 'sha256(  # AUTO-REMEDIATED: replaced md5 with sha256')
    },
]

# --- Scanner ---
def scan_directory(target_dir, auto_remediate=False):
    """
    This function recursively scans all files in the target directory for the patterns defined in MOCK_RULES.
    If auto_remediate is True, it will attempt to fix the findings using the remediation logic in each rule.
    Returns a list of findings (each is a dict with file, rule, desc, and severity).
    """
    findings = []  # Store all findings here
    for root, _, files in os.walk(target_dir):  # Walk through all directories and files
        for fname in files:
            path = os.path.join(root, fname)  # Full path to the file
            # Skip non-code files, like markdown, text, license, and this script itself
            if fname.endswith('.md') or fname.endswith('.txt') or fname.endswith('.rst') or fname == 'LICENSE' or fname == os.path.basename(__file__):
                continue
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()  # Read the file content
            except Exception as e:
                print(f"[WARN] Could not read {path}: {e}")  # Warn if file can't be read
                continue
            original_content = content  # Save the original content for comparison
            for rule in MOCK_RULES:
                # If the pattern is found in the file, record a finding
                if rule['pattern'] in content:
                    findings.append({'file': path, 'rule': rule['name'], 'desc': rule['desc'], 'severity': rule.get('severity', 'low')})
                    # If auto_remediate is enabled, apply the remediation function
                    if auto_remediate and 'remediate' in rule:
                        content = rule['remediate'](content)
            # If remediation changed the file, write it back
            if auto_remediate and content != original_content:
                try:
                    with open(path, 'w') as f:
                        f.write(content)
                    print(f"[AUTO-REMEDIATED] {path}")  # Log that we fixed this file
                except Exception as e:
                    print(f"[ERROR] Could not write {path}: {e}")  # Warn if we couldn't write
    return findings  # Return all findings

# --- Notifier ---
def notify(findings):
    """
    This function prints out the scan results in a friendly, color-coded way.
    It also determines if the result is PASSED, WARNED, or FAILED based on severity.
    """
    if not findings:
        # No findings, everything is good!
        print("\033[92mPASSED\033[0m: No vulnerabilities found. Safe to merge!")
        return "PASSED"
    else:
        # Check what kind of severities we have
        has_high = any(f['severity'] == 'high' for f in findings)
        has_medium = any(f['severity'] == 'medium' for f in findings)
        only_low = all(f['severity'] == 'low' for f in findings)
        # Decide the overall status
        if has_high or has_medium:
            status = "\033[91mFAILED\033[0m"  # Red for failed
        elif only_low:
            status = "\033[93mWARNED\033[0m"  # Yellow for warning
        else:
            status = "\033[93mWARNED\033[0m"  # Default to warning
        print(f"{status}: Vulnerabilities detected:")
        for f in findings:
            sev = f["severity"].upper()  # Show severity in uppercase
            print(f"- {f['file']} | {f['rule']} [{sev}]: {f['desc']}")  # Print each finding
        print("\nPlease remediate before merging.")  # Friendly reminder
        return status  # Return the status for use in main()

# --- CLI ---
def main():
    """
    This is the command-line entry point for the scanner.
    It parses arguments, runs the scan, prints results, and sets the exit code for CI/CD.
    """
    parser = argparse.ArgumentParser(description="Cloud Security Scanner for CI/CD pipelines")  # Set up the argument parser
    parser.add_argument('target', nargs='?', default='.', help='Target directory to scan')  # Where to scan
    parser.add_argument('--auto-remediate', '-f', action='store_true', help='Automatically fix vulnerabilities if possible')  # Auto-remediate flag
    args = parser.parse_args()  # Parse the arguments

    findings = scan_directory(args.target, auto_remediate=args.auto_remediate)  # Run the scan
    status = notify(findings)  # Print results and get status
    # Set the exit code for CI/CD: fail only if status is FAILED
    if status == "\033[91mFAILED\033[0m":
        exit(1)
    elif status == "\033[93mWARNED\033[0m":
        exit(0)
    else:
        exit(0)

# Standard Python entrypoint
if __name__ == "__main__":
    main()
