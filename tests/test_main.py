import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from src import main


class TaskCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tasks_file = Path(self.temp_dir.name) / "tasks.json"
        self.original_tasks_file = main.TASKS_FILE
        main.TASKS_FILE = self.tasks_file

    def tearDown(self) -> None:
        main.TASKS_FILE = self.original_tasks_file
        self.temp_dir.cleanup()

    def test_add_and_list_tasks(self) -> None:
        added = main.add_task("write tests", self.tasks_file)
        self.assertEqual(added["id"], 1)
        self.assertEqual(added["task"], "write tests")
        self.assertFalse(added["done"])

        tasks = main.list_tasks(self.tasks_file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(main.format_task(tasks[0]), "1. [ ] write tests")

    def test_done_marks_task_complete(self) -> None:
        main.add_task("ship feature", self.tasks_file)
        completed = main.mark_done(1, self.tasks_file)

        self.assertIsNotNone(completed)
        self.assertTrue(bool(completed["done"]))
        tasks = main.list_tasks(self.tasks_file)
        self.assertEqual(main.format_task(tasks[0]), "1. [x] ship feature")

    def test_run_cli_commands(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            add_exit = main.run_cli(["add", "first", "task"])
            list_exit = main.run_cli(["list"])
            done_exit = main.run_cli(["done", "1"])

        text = output.getvalue()
        self.assertEqual(add_exit, 0)
        self.assertEqual(list_exit, 0)
        self.assertEqual(done_exit, 0)
        self.assertIn("Added task 1.", text)
        self.assertIn("1. [ ] first task", text)
        self.assertIn("Completed task 1.", text)

    def test_run_cli_returns_error_for_bad_done_id(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main.run_cli(["done", "abc"])

        self.assertEqual(exit_code, 1)
        self.assertIn("Task id must be an integer.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
