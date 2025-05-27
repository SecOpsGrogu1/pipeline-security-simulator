# 🚨 Cloud Security Scanner for CI/CD Pipelines

A modern, single-file cloud security scanner for DevSecOps demos, interviews, and training. Inspired by Wiz and Prisma Cloud, this tool scans code for mock vulnerabilities, auto-remediates issues, and integrates seamlessly with CI/CD and GitOps workflows.

---

## 🏆 Key Features

- **All-in-one single file** (`main.py`): Easy to read, demo, and extend
- **Detects vulnerabilities**: Hardcoded secrets, insecure eval, weak hashes, and more
- **Severity levels**: Each finding is classified as HIGH, MEDIUM, or LOW
- **Auto-remediation**: Optionally fixes supported issues in place
- **CI/CD ready**: Fails or warns in pipelines based on severity
- **GitOps friendly**: All changes and policies are tracked in Git
- **Instant feedback**: Clear PASSED, WARNED, or FAILED status with details

---

## 🗂️ Architecture & Project Structure

```
pipeline-security-simulator/
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions workflow
├── main.py                # All scanner logic (rules, scan, remediation, notification)
├── requirements.txt       # Python dependencies (if any)
├── README.md              # Project info
```

---

## 🖼️ How It Works (Flow)

1. **Developer pushes code or opens a PR**
2. **CI/CD runs the scanner** (`main.py`)
3. **Scanner checks for vulnerabilities** and attempts auto-remediation if enabled
4. **Results:**
    - **PASSED:** No findings
    - **WARNED:** Only low-severity findings
    - **FAILED:** Any medium/high-severity findings
5. **Output is shown in CI logs**; merge is blocked if FAILED

---

## 🚀 Quick Start (Local Demo)

```sh
# 1. Clone the repo
 git clone <your-repo-url>
 cd pipeline-security-simulator

# 2. Install dependencies
 pip install -r requirements.txt

# 3. Add a test file with vulnerabilities
 echo 'SECRET_KEY = "mysecret"\nresult = eval("2+2")\nhash = md5(b"data").hexdigest()' > test_vuln.py

# 4. Run the scanner
 python main.py .

# 5. Try auto-remediation
 python main.py --auto-remediate .
```

---

## 🤖 Auto-Remediation Explained

- Use `--auto-remediate` or `-f` to enable auto-remediation.
- The scanner will attempt to fix supported vulnerabilities (e.g., redact secrets, comment out `eval`, replace `md5` with `sha256`).
- **Note:** In CI/CD, auto-remediation changes are not pushed back automatically. For true GitOps, pair with a bot or manual review process.

---

## 🛡️ Severity & Results Logic

- **Each finding** includes a `severity` (HIGH, MEDIUM, LOW)
- **Results:**
    - **PASSED:** No vulnerabilities
    - **WARNED:** Only low-severity vulnerabilities
    - **FAILED:** Any medium or high-severity vulnerabilities
- **CI/CD exit codes:**
    - `0` for PASSED/WARNED (pipeline continues)
    - `1` for FAILED (pipeline fails)

---

## 🔗 CI/CD Integration (GitHub Actions)

- Workflow: `.github/workflows/ci.yml`
- Runs on every push and PR
- Example step:
  ```yaml
  - name: Run Cloud Security Scanner (Auto-Remediate)
    run: |
      python main.py --auto-remediate .
  ```
- **Behavior:** If vulnerabilities remain after auto-remediation, the workflow fails (blocks merge).

---

## 🌀 GitOps Ready

- **All rules and logic are in Git**: Every change is auditable and reviewable
- **Policy as code**: Add or adjust rules in `main.py`, manage via PRs
- **Supports GitOps flows**: Optionally integrate with bots to open PRs with auto-remediation changes

---

## 🛠️ Customization

- **Add/Modify rules:** Edit the `MOCK_RULES` list in `main.py`
- **Ignore more files/dirs:** Update skip logic in `scan_directory()`
- **Notifications:** Extend `notify()` for Slack, email, or PR comments

---

## 👩‍💻 Example: Adding a Custom Rule

```python
MOCK_RULES = [
    # ... existing rules ...
    {
        'name': 'AWS Key',
        'pattern': 'AKIA',
        'desc': 'Possible AWS access key detected.',
        'severity': 'high',
        'remediate': lambda content: content.replace('AKIA', 'REDACTED_AWS_KEY')
    },
]
```

---

## 📸 Demo Workflow (for your presentation)

1. **Push a file with vulnerabilities (e.g., `test_vuln.py`)**
2. **Open a PR**
3. **CI/CD runs scanner**
4. **Output example:**
    ```
    [91mFAILED[0m: Vulnerabilities detected:
    - test_vuln.py | Hardcoded Secret [MEDIUM]: Possible hardcoded secret detected.
    - test_vuln.py | Insecure Function [HIGH]: Use of insecure eval() function.
    - test_vuln.py | Weak Hash [LOW]: Use of weak hash function md5.
    
    Please remediate before merging.
    ```
5. **Try auto-remediation locally, review changes, and commit fixes**

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
