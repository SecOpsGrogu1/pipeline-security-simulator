import os
from .rules import MOCK_RULES

def scan_directory(target_dir):
    """Scan all files in the directory for mock vulnerabilities."""
    findings = []
    for root, _, files in os.walk(target_dir):
        for fname in files:
            path = os.path.join(root, fname)
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                for rule in MOCK_RULES:
                    if rule['pattern'] in content:
                        findings.append({'file': path, 'rule': rule['name'], 'desc': rule['desc']})
    return findings
