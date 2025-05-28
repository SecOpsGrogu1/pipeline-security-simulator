# 🔐 Pipeline Security Simulator Demo

This repository demonstrates how to use **GitHub Actions** and **Trivy** to detect vulnerabilities in Docker images and enforce security gates in CI/CD. It mimics how tools like Wiz, Prisma Cloud, or Snyk might operate — failing builds, alerting teams, and optionally auto-remediating issues.

---

## 🚀 Overview

- **Two Dockerfiles:**
  - `Dockerfile.vuln`: Intentionally vulnerable (old OpenSSL on outdated Ubuntu)
  - `Dockerfile.clean`: Secure baseline image with minimal packages

- **GitHub Actions Workflow:**
  - Builds both Docker images
  - Scans with [Trivy](https://github.com/aquasecurity/trivy)
  - Outputs results as **SARIF** and uploads to GitHub **Code Scanning Alerts**
  - Fails pipeline on any **HIGH** or **CRITICAL** vulnerability in the vulnerable image

---

## ⚙️ How the Demo Works

1. On every `push` or `pull_request` to `main`:
   - Both images are built
   - Trivy scans them for vulnerabilities
   - If high/critical issues are found in `demo-vuln:latest`, the build fails
   - A SARIF report is uploaded to the Security tab in GitHub

2. Developers can then:
   - Review issues directly in the GitHub **Security > Code scanning alerts**
   - Fix the vulnerabilities and push again
   - On success, the pipeline passes ✅

---

## 📂 Files Included

- `Dockerfile.vuln` – Outdated Ubuntu + vulnerable OpenSSL
- `Dockerfile.clean` – Modern Ubuntu + safe packages
- `.github/workflows/docker-vuln-sarif.yml` – Main CI/CD workflow with Trivy + SARIF
- `trivy-results.sarif` – Output generated during workflow (not committed)

---

## 🧪 Usage

1. Clone this repo and push it to your GitHub
2. Open a PR or push to `main`
3. Watch GitHub Actions scan the images
4. View vulnerabilities in:
   - GitHub Security → Code Scanning Alerts (via SARIF)
   - GitHub Actions log

---

## 💡 Suggested Enhancements

This project is designed for learning and DevSecOps demos. You could extend it by:

- ✅ **Auto-creating Jira tickets** from failed builds
- ✅ **Notifying teams via Slack or MS Teams**
- ✅ **Auto-opening PRs to update base images** (using Renovate or a custom bot)
- ✅ **Scanning Infrastructure as Code** (Terraform, Kubernetes) with tools like `checkov` or `tfsec`

---

## ⚠️ Disclaimer

This setup is for educational purposes only.

---
