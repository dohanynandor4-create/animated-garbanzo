"""Entry point for animated-garbanzo."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """Runtime configuration loaded from environment values."""

    app_name: str
    environment: str
    debug_mode: bool
    runtime_checks: bool


def parse_bool(raw_value: str, default: bool = False) -> bool:
    """Parse a string as a boolean with a fallback default."""
    normalized = raw_value.strip().lower()
    if normalized in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "f", "no", "n", "off"}:
        return False
    return default


def parse_dotenv(path: str = ".env") -> dict[str, str]:
    """Parse simple KEY=VALUE lines from an optional .env file."""
    env_file = Path(path)
    if not env_file.exists():
        return {}

    parsed: dict[str, str] = {}
    for line in env_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue

        key, value = stripped.split("=", 1)
        key = key.strip()
        if not key:
            continue
        parsed[key] = value.strip().strip("\"'")

    return parsed


def load_config(dotenv_path: str = ".env") -> AppConfig:
    """Load config from environment, falling back to optional .env values."""
    dotenv_values = parse_dotenv(dotenv_path)

    def get_value(key: str, default: str) -> str:
        return os.environ.get(key, dotenv_values.get(key, default))

    return AppConfig(
        app_name=get_value("APP_NAME", "animated-garbanzo"),
        environment=get_value("APP_ENV", "development"),
        debug_mode=parse_bool(get_value("APP_DEBUG", "false")),
        runtime_checks=parse_bool(get_value("APP_RUNTIME_CHECKS", "true"), default=True),
    )


def describe_project() -> str:
    """Return a short description of the project state."""
    return "animated-garbanzo is ready for initial development."


def format_config(config: AppConfig) -> str:
    """Format the runtime config for display."""
    return (
        f"app name: {config.app_name}\n\n"
        f"environment: {config.environment}\n\n"
        f"debug mode: {config.debug_mode}\n\n"
        f"runtime checks: {config.runtime_checks}"
    )


if __name__ == "__main__":
    print(format_config(load_config()))
