# Cloud Security Scanner for CI/CD Pipelines

A lightweight, educational cloud security scanner inspired by Wiz and Prisma Cloud. This project is perfect for DevSecOps demos, interviews, and training. It scans code pushes for mock vulnerabilities, can auto-remediate issues, and integrates seamlessly with CI/CD pipelines.

---

## ✨ Features
- **Single-file design:** All logic in `main.py` for easy understanding and demoing
- **Scans code on every push/PR** for mock vulnerabilities (and can be extended to real rules)
- **Auto-remediation:** Optionally fixes supported vulnerabilities in place
- **Fails the CI/CD pipeline** if issues are found
- **Notifies developers** via console output (extendable to PR comments, Slack, etc.)
- **Minimal setup:** Just Python and a single script

---

## 📂 Project Structure
```
pipeline-security-simulator/
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions workflow
├── main.py               # All scanner logic (rules, scan, remediation, notification)
├── requirements.txt      # Python dependencies (if any)
├── README.md             # Project info
```

---

## 🚀 Quick Start (Local Demo)

1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd pipeline-security-simulator
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Add a test file with a mock vulnerability:**
   ```python
   # test_vuln.py
   SECRET_KEY = "mysecret"
   result = eval("2+2")
   hash = md5(b"data").hexdigest()
   ```

4. **Run the scanner:**
   ```sh
   python main.py .
   ```
   - If vulnerabilities are found, details are printed and the script exits with code 1.
   - If no issues are found, you'll see:
     ```
     ✅ No vulnerabilities found. Safe to merge!
     ```

5. **Try auto-remediation:**
   ```sh
   python main.py --auto-remediate .
   ```
   - Supported vulnerabilities will be fixed in place and logged.

---

## 🤖 Auto-Remediation

- Add `--auto-remediate` or `-f` to the CLI to enable auto-remediation.
- The scanner will attempt to fix supported vulnerabilities (e.g., redact secrets, comment out `eval`, replace `md5` with `sha256`).
- All changes are made in place—**always use version control!**

---

## ⚙️ How It Works
- **main.py:** Contains rules, scanning, remediation, and notification logic.
- Recursively scans files (skipping docs, LICENSE, and itself) for patterns defined in the rules section.
- If auto-remediation is enabled, fixes are applied and logged.
- Notifies results in the console and exits with code 1 if vulnerabilities remain (failing CI/CD pipelines).

---

## 🔗 CI/CD Integration (GitHub Actions)

- **Workflow:** `.github/workflows/ci.yml`
- **Runs:** On every push and pull request to `main`
- **Steps:**
  1. Checkout code
  2. Set up Python
  3. Install dependencies
  4. Run the scanner with auto-remediation:
     ```sh
     python main.py --auto-remediate .
     ```
- **Behavior:** If vulnerabilities are found and cannot be auto-remediated, the workflow fails and blocks merging until remediated.

---

## 🛠️ Customization

- **Add/Modify Rules:** Edit the `MOCK_RULES` list in `main.py`.
- **Ignore More Files/Dirs:** Update the skip logic in `scan_directory()`.
- **Notifications:** Extend the `notify()` function for Slack, email, or PR comments.

---

## 👩‍💻 Example: Adding a Custom Rule
```python
MOCK_RULES = [
    # ... existing rules ...
    {
        'name': 'AWS Key',
        'pattern': 'AKIA',
        'desc': 'Possible AWS access key detected.',
        'remediate': lambda content: content.replace('AKIA', 'REDACTED_AWS_KEY')
    },
]
```

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.

---

## 💡 Inspiration
Inspired by commercial tools like Wiz and Prisma Cloud, but designed for learning and demonstration purposes.

---

## 🚀 Quick Start (Local Demo)

1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd pipeline-security-simulator
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **(Optional) Add a test file with a mock vulnerability:**
   ```python
   # test_vuln.py
   SECRET_KEY="mysecret"
   ```

4. **Run the scanner:**
   ```sh
   python main.py .
   ```
   - If vulnerabilities are found, details are printed and the script exits with code 1.
   - If no issues are found, you'll see:
     ```
     ✅ No vulnerabilities found. Safe to merge!
     ```

---

## ⚙️ How It Works
- **scanner/scan.py:** Recursively scans all files in the target directory for patterns defined in `scanner/rules.py`.
- **scanner/rules.py:** Contains mock vulnerability rules (e.g., hardcoded secrets, use of `eval()`, weak hashes). Add your own for demos!
- **notify/notifier.py:** Prints findings to the console. Easily extend to notify via PR comments, Slack, etc.
- **main.py:** CLI entry point. Exits with code 1 if vulnerabilities are found (causes CI to fail).

---

## 🔗 CI/CD Integration (GitHub Actions)

This project comes with a ready-to-use GitHub Actions workflow:

- **Location:** `.github/workflows/ci.yml`
- **Triggers:** On every push and pull request to `main`
- **Steps:**
  1. Checkout code
  2. Set up Python
  3. Install dependencies
  4. Run the scanner
- **Behavior:** If vulnerabilities are found, the workflow fails and blocks merging until remediated.

**To use:**
- Push your code to GitHub
- Open a PR or push to `main`
- Check the Actions tab for results

---

## 🛠️ Customization

- **Add/Modify Rules:** Edit `scanner/rules.py` to add new patterns or adjust mock vulnerabilities.
- **Ignore Files/Dirs:** Update `scan.py` logic to skip certain files or directories (e.g., `__pycache__`, test files, etc.).
- **Notifications:** Extend `notifier.py` to send notifications to Slack, email, or GitHub PR comments.

---

## 👩‍💻 Example: Adding a Custom Rule
```python
# In scanner/rules.py
MOCK_RULES = [
    # ... existing rules ...
    {
        'name': 'AWS Key',
        'pattern': 'AKIA',
        'desc': 'Possible AWS access key detected.'
    },
]
```

---

## 🤝 Contributing
Pull requests and suggestions are welcome! This project is intentionally simple for educational/demo use, but feel free to fork and extend.

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.

---

## 🙋‍♂️ Why Use This?
- Perfect for DevSecOps demos and interviews
- Safe, mock vulnerabilities—no risk to real code
- Teachable, hackable, and easy to extend

---

## 💡 Inspiration
Inspired by commercial tools like Wiz and Prisma Cloud, but designed for learning and demonstration purposes.
