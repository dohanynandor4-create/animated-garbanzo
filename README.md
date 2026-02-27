# animated-garbanzo

## 1. Project overview
`animated-garbanzo` is a minimal Python CLI task tracker with local JSON persistence.

## 2. Prerequisites
- Git `>= 2.40`
- Python `>= 3.10`

## 3. Installation
```bash
# Clone the repository
git clone https://github.com/openai/codex.git
cd animated-garbanzo
```

No third-party dependencies are required.

## 4. Running locally
```bash
python -m src.main add "buy milk"
python -m src.main list
python -m src.main done 1
```

Tasks are stored in `tasks.json` in the current working directory.

## 5. Testing
```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## 6. Project structure
- `src/main.py` — CLI commands (`add`, `list`, `done`) and JSON persistence.
- `tests/test_main.py` — Unit tests for task operations and CLI handling.
- `README.md` — Project documentation and usage.
