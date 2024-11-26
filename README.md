
# Python Projects for Testing Vulnerabilities with Bandit

Welcome to our repository! This repository contains a collection of Python projects and JSON files designed to test and analyze security vulnerabilities using the **Bandit** static analysis tool. It serves as a comprehensive resource for exploring common vulnerabilities and evaluating Bandit's detection capabilities.

## 📋 Repository Contents

### 1. **Python Projects**
- A variety of Python scripts showcasing intentional vulnerabilities, such as:
  - Hardcoded secrets
  - SQL injection
  - Command injection
  - Insecure deserialization
  - Use of weak cryptographic algorithms
  - Cross-Site Scripting (XSS)
  - Server-Side Request Forgery (SSRF)

### 2. **JSON Files**
- Bandit output stored in JSON format designed for additional testing and analysis.

---

## 🚀 How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/viveksabbani/CAP6614_Final_Project.git
   cd CAP6614_Final_Project
   ```

2. **Run Bandit Analysis**
   Use Bandit to scan the Python files in the repository:
   ```bash
   bandit -r <project-directory>
   ```

3. **Evaluate Results**
   Review the output from Bandit to identify vulnerabilities and their severity levels.


---

## 👥 Contributors

This repository is maintained by our team as part of our project to evaluate Bandit. Below are the members of our group:

| **Name**            | **Role**                     |
|---------------------|-----------------------------|
| Vivek Sabbani       | Admin and Contributor |
| Tanmay Arora           | Contributor           |
| Shivam Singh       | Project Lead |
| Satwik Kaza          | Contributor           |
| Phaneendra Allu         | Contributor        |

Thank you for your contributions and collaboration!

---

## 📚 Documentation

- **Bandit Documentation**: [PyCQA Bandit Official Docs](https://bandit.readthedocs.io/)
- **OWASP Top Ten**: [OWASP Top Ten Vulnerabilities](https://owasp.org/www-project-top-ten/)

---

## 🤝 Contributions

We welcome contributions to improve our repository! Feel free to submit pull requests or open issues for suggestions and bug reports.

---

## 🛡️ Disclaimer

- This repository is for educational and research purposes only. The intentionally insecure code is provided to help developers and security professionals learn about vulnerabilities. Do not use this code in production environments.
- No copyright infringement intended, as we have used some open source and public code.
