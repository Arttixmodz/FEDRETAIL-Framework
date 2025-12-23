# Contributing to FEDRETAIL

Thank you for your interest in contributing to **FEDRETAIL**!  
Contributions from the research and industry community are highly welcome.

This document outlines how to contribute effectively and professionally.

---

## 🧭 Ways to Contribute

You can contribute by:

- 🐛 Reporting bugs or issues
- ✨ Proposing new features or improvements
- 📊 Adding experiments or benchmarks
- 📚 Improving documentation
- 🧪 Adding tests or improving reproducibility
- 🔐 Proposing security or privacy enhancements

---

## 🛠 Development Setup

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/<your-username>/FEDRETAIL.git
cd FEDRETAIL
```
3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📐 Coding Standards

To maintain code quality and long-term maintainability, please follow these guidelines:

* Write **clean, modular, and well-documented** code
* Follow **PEP 8** coding standards for Python
* Add **docstrings** to all public functions and classes
* Avoid **hard-coded values**; prefer configurable parameters
* Ensure new changes **do not break existing experiments or results**

---

## 🧪 Experiments & Research Contributions

If you are contributing experiments or benchmarks:

* Clearly describe the **experimental setup**
* Specify the **dataset, parameters, and assumptions**
* Ensure results are **reproducible**
* Add generated plots under `docs/results/` with **clear captions**

---

## 🔄 Pull Request Process

1. Create a new feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Commit your changes with **clear and descriptive messages**

3. Push the branch to your fork

4. Open a **Pull Request (PR)** including:

   * Clear description of the change
   * Motivation and expected impact
   * Related issues (if any)

### All pull requests are reviewed for:

* Code quality and clarity
* Correctness and stability
* Reproducibility of results
* Alignment with FEDRETAIL’s research and engineering goals

---

## 📜 Licensing

By contributing to this project, you agree that your contributions will be licensed under the **same license** as the FEDRETAIL project.

---

## 🙏 Acknowledgement

All contributors will be **acknowledged appropriately**.
Significant research or engineering contributions may be **recognized in future publications**.

Thank you for helping improve **FEDRETAIL** 🚀
