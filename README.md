# animated-garbanzo

## 1. Project overview
`animated-garbanzo` is a minimal Python starter project with a runnable entry point and a unit test suite.

## 2. Prerequisites
- Git `>= 2.40`
- Python `>= 3.10`

## 3. Installation
```bash
# Clone the repository
git clone https://github.com/openai/codex.git
cd animated-garbanzo
```

No third-party dependencies are required right now.

## 4. Running locally
```bash
# Default description output
python -m src.main
# expected output:
# animated-garbanzo is ready for initial development.

# Human-readable status
python -m src.main --status
# expected output (example):
# project: animated-garbanzo
# description: animated-garbanzo is ready for initial development.
# python: 3.11.11

# Human-readable checks
python -m src.main --check
# expected output (example):
# python_version_supported: PASS
# tests_present: PASS

# Machine-readable status + checks
python -m src.main --status --check --json
# expected output (example):
# {
#   "checks": {
#     "python_version_supported": true,
#     "tests_present": true
#   },
#   "status": {
#     "description": "animated-garbanzo is ready for initial development.",
#     "project": "animated-garbanzo",
#     "python": "3.11.11"
#   }
# }
```

## 5. Testing
```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## 6. Project structure
Current repository contents:

- `src/main.py` — App entry point with core project description function.
- `tests/test_main.py` — Unit tests for the entry point logic.
- `README.md` — Project documentation and onboarding instructions.

## 7. Contributing
Use the following baseline process:

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/<short-description>
   ```
2. Make focused, atomic commits with clear messages:
   ```bash
   git add <files>
   git commit -m "feat: describe change"
   ```
3. Run all required tests/lint checks (see **Testing**).
4. Open a pull request that includes:
   - A concise summary of what changed.
   - Test evidence (commands run + results).
   - Any follow-up TODOs or known limitations.

## 8. License
License TBD.
