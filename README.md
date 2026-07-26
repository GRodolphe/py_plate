# py_plate

[![CI](https://github.com/GRodolphe/py_plate/workflows/CI/badge.svg)](https://github.com/GRodolphe/py_plate/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/GRodolphe/py_plate/branch/main/graph/badge.svg)](https://codecov.io/gh/GRodolphe/py_plate)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

<img src="img/py_plate.png" alt="py_plate" width="200">

A modern Python CLI template with best practices, featuring Typer, Ruff, pre-commit hooks, and comprehensive tooling setup.

## ✨ Features

- 🚀 **Modern CLI** with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)
- 🔧 **Development tools** with [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- 🛡️ **Security** with pre-commit hooks and secret detection
- 🧪 **Testing** with pytest and coverage reporting
- 📦 **Easy installation** with uv support
- 🎯 **Type safety** with mypy
- 📋 **Code quality** with comprehensive linting rules
- 🚀 **CI/CD** with GitHub Actions for testing, linting, and releases
- 📊 **Coverage reporting** with Codecov integration

## 🛡️ Security Tools

This template includes comprehensive security scanning tools that run automatically in CI/CD pipelines and can be used during development:

- **[OSV-Scanner](https://osv.dev/)** - Vulnerability scanner based on the OSV.dev database
  - Scans for known vulnerabilities in dependencies
  - Uploads results to the GitHub Security tab via SARIF
  - Integrated into CI pipeline and as a release gate

- **[Bandit](https://bandit.readthedocs.io/)** - Security linter for Python code
  - Identifies common security issues in Python code
  - Configurable via `pyproject.toml`
  - Runs automatically in CI pipeline

- **[Safety](https://pyup.io/safety/)** - Dependency vulnerability scanner
  - Checks Python dependencies against known security vulnerabilities
  - Integrates with requirements and package files
  - Provides detailed vulnerability reports

- **[detect-secrets](https://github.com/Yelp/detect-secrets)** - Prevents secrets from being committed
  - Scans for API keys, tokens, and other sensitive data
  - Uses baseline file to track known false positives
  - Runs as pre-commit hook and in CI pipeline

All security tools generate JSON reports that are included as artifacts in GitHub releases, providing transparency and audit trails for security compliance.

## 🚀 Quick Start with uv

[uv](https://docs.astral.sh/uv/) is the recommended way to install Python CLI applications. Its `uv tool` command installs packages in isolated environments while making their entry points available globally.

### Install uv (if not already installed)

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On macOS with Homebrew
brew install uv

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip
pip install uv
```

### Install the CLI

```bash
# Install from PyPI (when published)
uv tool install py-plate-template

# Or install from local directory
uv tool install .

# Or install in development mode
uv tool install --editable .
```

### Usage

```bash
# Show help
py-plate --help

# Greet someone
py-plate hello Alice

# Greet with options
py-plate hello Bob --count 3 --shout

# Show system information
py-plate info

# Show version
py-plate --version

# Manage configuration
py-plate config --show
py-plate config --set debug true
```

## 🛠️ Development Setup

### Prerequisites

- Python 3.9 or higher
- uv (recommended) or pip

### Development Installation

```bash
# Clone the repository
git clone https://github.com/GRodolphe/py_plate.git
cd py_plate

# Install in development mode with all dependencies
pip install -e ".[dev]"

# Or use uv for isolated development
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Set up pre-commit hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks on all files (optional)
pre-commit run --all-files
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_cli.py

# Run with verbose output
pytest -v
```

## 🔧 Development Commands

```bash
# Format code
ruff format

# Lint code
ruff check

# Fix linting issues automatically
ruff check --fix

# Type check
mypy src/

# Run all quality checks
ruff check && ruff format --check && mypy src/ && pytest
```

## 📦 Building and Publishing

```bash
# Build the package
python -m build

# Upload to PyPI (requires authentication)
python -m twine upload dist/*
```

## 🏗️ Project Structure

```
py_plate/
├── src/
│   └── py_plate/
│       ├── __init__.py          # Package version and metadata
│       └── cli.py               # Main CLI application
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest configuration and fixtures
│   └── test_cli.py              # CLI tests
├── .gitignore                   # Git ignore rules
├── .pre-commit-config.yaml      # Pre-commit hooks configuration
├── .secrets.baseline            # Secrets detection baseline
├── pyproject.toml               # Project configuration and dependencies
└── README.md                    # This file
```

## ⚙️ Configuration

The project uses `pyproject.toml` for all configuration:

- **Build system**: Hatchling
- **Dependencies**: Typer, Rich
- **Development tools**: Ruff, mypy, pytest
- **Code quality**: Pre-commit hooks with multiple checkers

### Key Configuration Sections

- **Ruff**: Linting and formatting rules
- **Pytest**: Test configuration and coverage
- **MyPy**: Type checking settings
- **Pre-commit**: Hook definitions for code quality

## 🚀 GitHub Actions Workflows

The template includes comprehensive CI/CD pipelines:

### CI Pipeline (`ci.yml`)
- **Multi-version testing**: Tests against Python 3.9, 3.10, 3.11, and 3.12
- **Code quality**: Ruff linting and formatting checks
- **Type safety**: MyPy type checking
- **Test coverage**: Pytest with coverage reporting
- **Security scanning**: Bandit and Safety checks
- **Secret detection**: Automated secret scanning
- **Build verification**: Package building and artifact upload

### Release Pipeline (`release.yml`)
- **Automated releases**: Triggered on version tags
- **PyPI publishing**: Automatic package publishing
- **GitHub releases**: Automated release notes generation
- **Pre-release validation**: Full test suite before release

### Pre-commit Pipeline (`pre-commit.yml`)
- **Code quality gates**: Automated pre-commit hook validation
- **Consistent formatting**: Ensures code standards across contributions

## 🔒 Security Features

- **Secret detection** with detect-secrets
- **Dependency vulnerability scanning** with Safety
- **Security linting** with Bandit
- **Pre-commit hooks** for automated checking
- **Automated security scans** in CI pipeline

## 🎯 Best Practices Included

- **Type hints** throughout the codebase
- **Comprehensive error handling**
- **Rich console output** for better UX
- **Structured logging** ready for implementation
- **Configuration management** pattern
- **Test coverage** tracking
- **Documentation** with examples

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the test suite
5. Submit a pull request

The pre-commit hooks will automatically run code quality checks on each commit.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
