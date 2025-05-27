def notify(findings):
    if not findings:
        print("✅ No vulnerabilities found. Safe to merge!")
    else:
        print("❌ Vulnerabilities detected:")
        for f in findings:
            print(f"- {f['file']} | {f['rule']}: {f['desc']}")
        print("\nPlease remediate before merging.")
