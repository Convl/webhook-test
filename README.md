# Simple Calculator

A basic command-line calculator application written in Python.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide, power)
- Advanced operations (square root, factorial)
- Interactive command-line interface
- Error handling for invalid inputs
- Unit tests included
- CI/CD pipeline with automated testing

## Usage

Run the calculator:
```bash
python main.py
```

Run tests:
```bash
python test_calculator.py
```

Or with pytest:
```bash
pytest test_calculator.py
```

## Development

Install development dependencies:
```bash
pip install -r requirements.txt
```

Run linting:
```bash
flake8 .
pylint calculator.py main.py test_calculator.py
```

## CI/CD

This project uses GitHub Actions for continuous integration:

- **Automated Testing**: Runs on every push and pull request
- **Multi-Python Support**: Tests against Python 3.8, 3.9, 3.10, 3.11, and 3.12
- **Code Quality**: Includes flake8 and pylint checks
- **Syntax Validation**: Ensures all Python files compile correctly
- **Smart Caching**: Optimized dependency caching for faster builds

### Pipeline Details

The CI pipeline consists of two parallel jobs:

#### Test Job (Multi-Python)
1. **Matrix Testing**: Runs tests across 5 Python versions (3.8-3.12)
2. **Dependency Caching**: Caches pip packages per Python version for faster builds
3. **Pytest Testing**: Runs comprehensive unit tests with detailed output
4. **Syntax Validation**: Ensures all Python files compile correctly
5. **Format Checking**: Verifies code formatting with Black

#### Lint Job (Code Quality)
1. **Dependency Caching**: Separate cache for linting tools
2. **Flake8**: Fast style and basic error checking
3. **Pylint**: Comprehensive code analysis and complexity checking

### Caching Strategy

- **Test Job Cache**: `ubuntu-pip-{python-version}-{requirements-hash}`
- **Lint Job Cache**: `ubuntu-pip-lint-{requirements-hash}`
- **Cache Invalidation**: When requirements.txt changes or after 7 days of inactivity
- **Fallback**: Uses most recent compatible cache if exact match not found

## Structure

- `calculator.py` - Core calculator functions
- `main.py` - CLI interface
- `test_calculator.py` - Unit tests
- `requirements.txt` - Dependencies
- `.github/workflows/ci.yml` - CI/CD pipeline configuration
- `setup.cfg` - Linting tool configurations

## Future Features

- [ ] Memory functions (store/recall)
- [ ] History of calculations
- [ ] Scientific calculator functions
- [ ] GUI interface
- [ ] Web API 