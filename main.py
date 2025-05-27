import os
import argparse
import sys

# --- Rules ---
MOCK_RULES = [
    {
        'name': 'Hardcoded Secret',
        'pattern': 'SECRET_KEY=',
        'desc': 'Possible hardcoded secret detected.',
        'remediate': lambda content: content.replace('SECRET_KEY=', 'SECRET_KEY="REDACTED_AUTO_REMEDIATED" # ')
    },
    {
        'name': 'Insecure Function',
        'pattern': 'eval(',
        'desc': 'Use of insecure eval() function.',
        'remediate': lambda content: content.replace('eval(', '# eval(  # AUTO-REMEDIATED: removed insecure eval')
    },
    {
        'name': 'Weak Hash',
        'pattern': 'md5(',
        'desc': 'Use of weak hash function md5.',
        'remediate': lambda content: content.replace('md5(', 'sha256(  # AUTO-REMEDIATED: replaced md5 with sha256')
    },
]

# --- Scanner ---
def scan_directory(target_dir, auto_remediate=False):
    """
    Scan all files in the directory for mock vulnerabilities.
    If auto_remediate is True, attempt to automatically fix findings using rule['remediate'].
    """
    findings = []
    for root, _, files in os.walk(target_dir):
        for fname in files:
            path = os.path.join(root, fname)
            # Skip non-code files (README, LICENSE, etc.) and self
            if fname.endswith('.md') or fname.endswith('.txt') or fname.endswith('.rst') or fname == 'LICENSE' or fname == os.path.basename(__file__):
                continue
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                print(f"[WARN] Could not read {path}: {e}")
                continue
            original_content = content
            for rule in MOCK_RULES:
                if rule['pattern'] in content:
                    findings.append({'file': path, 'rule': rule['name'], 'desc': rule['desc']})
                    if auto_remediate and 'remediate' in rule:
                        content = rule['remediate'](content)
            if auto_remediate and content != original_content:
                try:
                    with open(path, 'w') as f:
                        f.write(content)
                    print(f"[AUTO-REMEDIATED] {path}")
                except Exception as e:
                    print(f"[ERROR] Could not write {path}: {e}")
    return findings

# --- Notifier ---
def notify(findings):
    if not findings:
        print(" No vulnerabilities found. Safe to merge!")
    else:
        print(" Vulnerabilities detected:")
        for f in findings:
            print(f"- {f['file']} | {f['rule']}: {f['desc']}")
        print("\nPlease remediate before merging.")

# --- CLI ---
def main():
    parser = argparse.ArgumentParser(description="Cloud Security Scanner for CI/CD pipelines")
    parser.add_argument('target', nargs='?', default='.', help='Target directory to scan')
    parser.add_argument('--auto-remediate', '-f', action='store_true', help='Automatically fix vulnerabilities if possible')
    args = parser.parse_args()

    findings = scan_directory(args.target, auto_remediate=args.auto_remediate)
    notify(findings)
    if findings:
        exit(1)

if __name__ == "__main__":
    main()
