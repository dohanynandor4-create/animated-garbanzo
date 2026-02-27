"""Simple task CLI with JSON persistence."""

from __future__ import annotations

import json
import sys
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks(tasks_file: Path = TASKS_FILE) -> list[dict[str, object]]:
    """Load tasks from disk; return an empty list if missing or invalid."""
    if not tasks_file.exists():
        return []

    try:
        data = json.loads(tasks_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

    if not isinstance(data, list):
        return []

    return data


def save_tasks(tasks: list[dict[str, object]], tasks_file: Path = TASKS_FILE) -> None:
    """Persist tasks to disk as pretty JSON."""
    tasks_file.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def add_task(task_text: str, tasks_file: Path = TASKS_FILE) -> dict[str, object]:
    """Add a new task and persist it."""
    tasks = load_tasks(tasks_file)
    next_id = max((int(task["id"]) for task in tasks), default=0) + 1
    new_task = {"id": next_id, "task": task_text, "done": False}
    tasks.append(new_task)
    save_tasks(tasks, tasks_file)
    return new_task


def list_tasks(tasks_file: Path = TASKS_FILE) -> list[dict[str, object]]:
    """Return all persisted tasks."""
    return load_tasks(tasks_file)


def mark_done(task_id: int, tasks_file: Path = TASKS_FILE) -> dict[str, object] | None:
    """Mark a task complete by id and persist; return None if not found."""
    tasks = load_tasks(tasks_file)
    for task in tasks:
        if int(task.get("id", -1)) == task_id:
            task["done"] = True
            save_tasks(tasks, tasks_file)
            return task
    return None


def format_task(task: dict[str, object]) -> str:
    """Format a task for terminal output."""
    status = "x" if task.get("done") else " "
    return f"{task.get('id')}. [{status}] {task.get('task')}"


def run_cli(argv: list[str]) -> int:
    """Run CLI command and return process exit code."""
    if not argv:
        print("Usage: add <task> | list | done <id>")
        return 1

    command = argv[0]

    if command == "add":
        if len(argv) < 2:
            print("Usage: add <task>")
            return 1
        task = add_task(" ".join(argv[1:]))
        print(f"Added task {task['id']}.")
        return 0

    if command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks.")
            return 0
        for task in tasks:
            print(format_task(task))
        return 0

    if command == "done":
        if len(argv) != 2:
            print("Usage: done <id>")
            return 1
        try:
            task_id = int(argv[1])
        except ValueError:
            print("Task id must be an integer.")
            return 1

        task = mark_done(task_id)
        if task is None:
            print(f"Task {task_id} not found.")
            return 1

        print(f"Completed task {task_id}.")
        return 0

    print("Usage: add <task> | list | done <id>")
    return 1


if __name__ == "__main__":
    raise SystemExit(run_cli(sys.argv[1:]))
