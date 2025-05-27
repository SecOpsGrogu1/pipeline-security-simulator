import sys
from scanner.scan import scan_directory
from notify.notifier import notify

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    findings = scan_directory(target_dir)
    notify(findings)
    if findings:
        exit(1)

if __name__ == "__main__":
    main()
