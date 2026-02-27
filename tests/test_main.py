import io
import json
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from src.main import describe_project, main, run_checks


class DescribeProjectTests(unittest.TestCase):
    def test_describe_project_returns_expected_message(self) -> None:
        self.assertEqual(
            describe_project(),
            "animated-garbanzo is ready for initial development.",
        )


class MainCliTests(unittest.TestCase):
    def test_main_without_args_prints_default_description(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            buffer.getvalue().strip(),
            "animated-garbanzo is ready for initial development.",
        )

    def test_status_outputs_human_readable_details(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main(["--status"])

        output = buffer.getvalue()
        self.assertEqual(exit_code, 0)
        self.assertIn("project: animated-garbanzo", output)
        self.assertIn("description: animated-garbanzo is ready for initial development.", output)
        self.assertIn("python:", output)

    def test_check_outputs_human_readable_pass_states(self) -> None:
        buffer = io.StringIO()
        with patch(
            "src.main.run_checks",
            return_value={"python_version_supported": True, "tests_present": True},
        ):
            with redirect_stdout(buffer):
                exit_code = main(["--check"])

        self.assertEqual(exit_code, 0)
        self.assertIn("python_version_supported: PASS", buffer.getvalue())
        self.assertIn("tests_present: PASS", buffer.getvalue())

    def test_status_and_check_as_json(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main(["--status", "--check", "--json"])

        self.assertEqual(exit_code, 0)
        payload = json.loads(buffer.getvalue())
        self.assertIn("status", payload)
        self.assertIn("checks", payload)
        self.assertEqual(payload["status"]["project"], "animated-garbanzo")

    def test_status_only_as_json_has_status_payload(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main(["--status", "--json"])

        self.assertEqual(exit_code, 0)
        payload = json.loads(buffer.getvalue())
        self.assertIn("status", payload)
        self.assertNotIn("checks", payload)

    def test_check_only_as_json_has_checks_payload(self) -> None:
        buffer = io.StringIO()
        with patch(
            "src.main.run_checks",
            return_value={"python_version_supported": True, "tests_present": True},
        ):
            with redirect_stdout(buffer):
                exit_code = main(["--check", "--json"])

        self.assertEqual(exit_code, 0)
        payload = json.loads(buffer.getvalue())
        self.assertIn("checks", payload)
        self.assertEqual(payload["checks"]["python_version_supported"], True)

    def test_check_returns_failure_exit_code_when_a_check_fails(self) -> None:
        buffer = io.StringIO()
        with patch(
            "src.main.run_checks",
            return_value={"python_version_supported": False, "tests_present": True},
        ):
            with redirect_stdout(buffer):
                exit_code = main(["--check"])

        self.assertEqual(exit_code, 1)
        self.assertIn("python_version_supported: FAIL", buffer.getvalue())

    def test_check_returns_failure_exit_code_when_a_check_fails_with_json(self) -> None:
        buffer = io.StringIO()
        with patch(
            "src.main.run_checks",
            return_value={"python_version_supported": False, "tests_present": True},
        ):
            with redirect_stdout(buffer):
                exit_code = main(["--check", "--json"])

        self.assertEqual(exit_code, 1)
        payload = json.loads(buffer.getvalue())
        self.assertEqual(payload["checks"]["python_version_supported"], False)

    def test_invalid_argument_raises_system_exit(self) -> None:
        with self.assertRaises(SystemExit) as ctx:
            main(["--unknown-flag"])

        self.assertNotEqual(ctx.exception.code, 0)


class ChecksTests(unittest.TestCase):
    def test_run_checks_contains_expected_keys(self) -> None:
        checks = run_checks()
        self.assertIn("python_version_supported", checks)
        self.assertIn("tests_present", checks)


if __name__ == "__main__":
    unittest.main()
