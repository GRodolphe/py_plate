# Security Policy

## Supported Versions

We actively support the following versions of py_plate with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of py_plate seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **GitHub Security Advisories** (Preferred)
   - Go to the [Security tab](https://github.com/GRodolphe/py_plate/security) of this repository
   - Click "Report a vulnerability"
   - Fill out the vulnerability report form

2. **Email**
   - Send an email to: [contact@rodolpheg.xyz](mailto:contact@rodolpheg.xyz)
   - Include the word "SECURITY" in the subject line

### What to Include

Please include the following information in your report:

- **Description**: A clear description of the vulnerability
- **Impact**: What kind of vulnerability it is and which system components are affected
- **Reproduction**: Step-by-step instructions to reproduce the issue
- **Environment**: Version of py_plate, Python version, operating system
- **Proof of Concept**: Any proof-of-concept or exploit code (if available)

### Response Timeline

- **Initial Response**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Investigation**: We will investigate and validate the reported vulnerability within 5 business days
- **Resolution**: We will work to resolve confirmed vulnerabilities as quickly as possible, typically within 30 days
- **Disclosure**: We will coordinate with you on the disclosure timeline

### Security Measures

py_plate implements several security measures:

- **Dependency Scanning**: Automated vulnerability scanning of dependencies using Safety and Trivy
- **Static Analysis**: Code security analysis using Bandit
- **Secret Detection**: Automated detection of exposed secrets using detect-secrets
- **Pre-commit Hooks**: Security checks run before each commit
- **CI/CD Security**: Comprehensive security scanning in our CI/CD pipeline

### Responsible Disclosure

We believe in responsible disclosure of security vulnerabilities. We ask that you:

- Give us reasonable time to investigate and fix the issue before making it public
- Make a good faith effort to avoid privacy violations, destruction of data, and disruption of our systems
- Contact us before engaging in any security testing of our systems

### Recognition

We appreciate the security research community's efforts to improve the security of open source software. Security researchers who responsibly disclose vulnerabilities will be:

- Credited in our security advisories (unless they prefer to remain anonymous)
- Listed in our project acknowledgments
- Invited to test our fixes before public release

## Security Best Practices for Users

### Installation

- Always install py_plate from official sources (PyPI, GitHub releases)
- Verify package integrity when possible
- Keep py_plate updated to the latest version

### Usage

- Follow the principle of least privilege when running py_plate
- Regularly audit your dependencies for known vulnerabilities
- Use virtual environments to isolate py_plate from other packages

### Configuration

- Never commit sensitive information (API keys, passwords, tokens) to version control
- Use environment variables or secure secret management for sensitive configuration
- Review and understand any configuration files before use

## Contact

For any questions about this security policy, please contact:
- Email: [contact@rodolpheg.xyz](mailto:contact@rodolpheg.xyz)
- GitHub: [@GRodolphe](https://github.com/GRodolphe)

---

*This security policy is effective as of the date of the latest commit to this file and will be updated as needed.*
