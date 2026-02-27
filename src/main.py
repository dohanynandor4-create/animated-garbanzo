"""Entry point for animated-garbanzo."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path

SUPPORTED_PYTHON_MAJOR = 3
SUPPORTED_PYTHON_MINOR = 10


def describe_project() -> str:
    """Return a short description of the project state."""
    return "animated-garbanzo is ready for initial development."


def project_status() -> dict[str, str]:
    """Build a project status payload."""
    return {
        "project": "animated-garbanzo",
        "description": describe_project(),
        "python": platform.python_version(),
    }


def run_checks() -> dict[str, bool]:
    """Run simple environment checks."""
    version_ok = sys.version_info >= (SUPPORTED_PYTHON_MAJOR, SUPPORTED_PYTHON_MINOR)
    tests_present = Path("tests/test_main.py").exists()
    return {
        "python_version_supported": version_ok,
        "tests_present": tests_present,
    }


def build_parser() -> argparse.ArgumentParser:
    """Create and return the CLI parser."""
    parser = argparse.ArgumentParser(description="animated-garbanzo utility CLI")
    parser.add_argument(
        "--status",
        action="store_true",
        help="Print a human-readable project status summary.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run environment checks and print their result.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Render output as JSON (use with --status and/or --check).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return an exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.status and not args.check:
        print(describe_project())
        return 0

    output: dict[str, object] = {}
    if args.status:
        output["status"] = project_status()
    if args.check:
        checks = run_checks()
        output["checks"] = checks
        if not all(checks.values()):
            if args.json:
                print(json.dumps(output, indent=2, sort_keys=True))
            else:
                for name, passed in checks.items():
                    state = "PASS" if passed else "FAIL"
                    print(f"{name}: {state}")
            return 1

    if args.json:
        print(json.dumps(output, indent=2, sort_keys=True))
    else:
        if args.status:
            status = output["status"]
            print(f"project: {status['project']}")
            print(f"description: {status['description']}")
            print(f"python: {status['python']}")
        if args.check:
            checks = output["checks"]
            for name, passed in checks.items():
                state = "PASS" if passed else "FAIL"
                print(f"{name}: {state}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
