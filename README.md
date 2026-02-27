# animated-garbanzo

## 1. Project overview
`animated-garbanzo` is a minimal Python starter project with a runnable entry point and a unit test suite.

The app reads runtime config from environment variables (with optional `.env` fallback), prints core runtime values, and can emit a small health report.

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

## 4. Configuration
Supported configuration keys:

- `APP_NAME` (default: `animated-garbanzo`)
- `APP_ENV` (default: `development`)
- `APP_DEBUG` (default: `false`)
- `APP_RUNTIME_CHECKS` (default: `true`)

Environment variables override values from `.env`.

Example `.env`:
```dotenv
APP_NAME=animated-garbanzo
APP_ENV=development
APP_DEBUG=false
APP_RUNTIME_CHECKS=true
```

## 5. Running locally
```bash
python -m src.main
```

When runtime checks are enabled, the app also prints a health report with:
- Python version supported
- Writable project directory
- Tests present

## 6. Testing
```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## 7. Project structure
Current repository contents:

- `src/main.py` — App entry point with env config loading and runtime health checks.
- `tests/test_main.py` — Unit tests for config parsing, formatting, and health-check behavior.
- `README.md` — Project documentation and onboarding instructions.

## 8. Contributing
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

## 9. License
License TBD.
