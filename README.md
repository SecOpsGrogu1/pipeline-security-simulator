# Cloud Security Scanner for CI/CD Pipelines

A lightweight, educational cloud security scanner that mimics tools like Wiz or Prisma Cloud. This project is designed for DevSecOps demos, interviews, and training—scanning code pushes for mock vulnerabilities and failing the pipeline if issues are found. Developers are notified to remediate before merging, simulating a real-world DevSecOps workflow.

---

## ✨ Features
- **Scans code on every push/PR** for mock vulnerabilities (easily extendable to real rules)
- **Fails the CI/CD pipeline** if issues are found
- **Notifies developers** via console output (extendable to PR comments, Slack, etc.)
- **Easy to demo** locally or in CI/CD environments
- **Modular, readable code** for educational use

---

## 📂 Project Structure
```
pipeline-security-simulator/
├── scanner/
│   ├── __init__.py
│   ├── scan.py           # Scanning logic
│   └── rules.py          # Mock vulnerability rules
├── notify/
│   ├── __init__.py
│   └── notifier.py       # Notification logic
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions workflow
├── main.py               # CLI entry point
├── requirements.txt      # Python dependencies
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
