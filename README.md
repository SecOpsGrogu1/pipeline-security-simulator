# Pipeline Security Simulator Demo

This repository demonstrates how to use GitHub Actions and Trivy to detect vulnerabilities in Docker images and fail the CI pipeline if issues are found.

## Overview
- **Two Dockerfiles:**
  - `Dockerfile.vuln`: Intentionally uses an outdated Ubuntu base and installs a vulnerable version of OpenSSL.
  - `Dockerfile.clean`: Uses an up-to-date Ubuntu base and only installs safe packages.
- **GitHub Actions Pipeline:**
  - Builds both images.
  - Scans each image with [Trivy](https://github.com/aquasecurity/trivy).
  - Fails the pipeline if high/critical vulnerabilities are found in the vulnerable image.

## How the Demo Works
1. **On push or pull request to `main`:**
   - The workflow builds both Docker images.
   - Trivy scans both images for vulnerabilities.
   - If high/critical vulnerabilities are found in `demo-vuln:latest`, the pipeline fails (as expected for demo purposes).
   - The clean image should pass the scan.

## Files
- `Dockerfile.vuln`: Vulnerable Dockerfile (outdated Ubuntu + old OpenSSL)
- `Dockerfile.clean`: Clean Dockerfile (latest Ubuntu + only ca-certificates)
- `.github/workflows/docker-vuln-demo.yml`: GitHub Actions workflow

## Usage
1. **Push this repository to GitHub.**
2. **Ensure GitHub Actions is enabled.**
3. **Open a Pull Request or push to `main`.**
4. **Observe the workflow:**
    - The scan on the vulnerable image will detect issues and fail the pipeline.
    - The scan on the clean image should pass.

## Customization
- To demo different vulnerabilities, modify `Dockerfile.vuln` to install other outdated or vulnerable packages.
- To test different scanners, swap out Trivy for another tool in the workflow.

---

**This setup is for demonstration purposes only. Never use intentionally vulnerable images in production!**
