import os
import tempfile
import unittest

from src.main import AppConfig, describe_project, format_config, load_config, parse_bool, parse_dotenv


class DescribeProjectTests(unittest.TestCase):
    def test_describe_project_returns_expected_message(self) -> None:
        self.assertEqual(
            describe_project(),
            "animated-garbanzo is ready for initial development.",
        )


class ParseBoolTests(unittest.TestCase):
    def test_parse_bool_true_values(self) -> None:
        self.assertTrue(parse_bool("true"))
        self.assertTrue(parse_bool("On"))
        self.assertTrue(parse_bool("1"))

    def test_parse_bool_false_values(self) -> None:
        self.assertFalse(parse_bool("false", default=True))
        self.assertFalse(parse_bool("off", default=True))
        self.assertFalse(parse_bool("0", default=True))

    def test_parse_bool_invalid_uses_default(self) -> None:
        self.assertTrue(parse_bool("not-a-bool", default=True))
        self.assertFalse(parse_bool("not-a-bool", default=False))


class ParseDotenvTests(unittest.TestCase):
    def test_parse_dotenv_reads_simple_key_values(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = os.path.join(tmpdir, ".env")
            with open(env_path, "w", encoding="utf-8") as env_file:
                env_file.write("# comment\nAPP_NAME=demo\nAPP_DEBUG='true'\nINVALID\n")

            parsed = parse_dotenv(env_path)

        self.assertEqual(parsed["APP_NAME"], "demo")
        self.assertEqual(parsed["APP_DEBUG"], "true")
        self.assertNotIn("INVALID", parsed)


class LoadConfigTests(unittest.TestCase):
    def test_load_config_prefers_os_environment_over_dotenv(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = os.path.join(tmpdir, ".env")
            with open(env_path, "w", encoding="utf-8") as env_file:
                env_file.write("APP_NAME=from_dotenv\nAPP_ENV=staging\nAPP_DEBUG=true\n")

            old_env = os.environ.copy()
            os.environ["APP_NAME"] = "from_os"
            os.environ["APP_RUNTIME_CHECKS"] = "false"
            try:
                config = load_config(env_path)
            finally:
                os.environ.clear()
                os.environ.update(old_env)

        self.assertEqual(config.app_name, "from_os")
        self.assertEqual(config.environment, "staging")
        self.assertTrue(config.debug_mode)
        self.assertFalse(config.runtime_checks)


class FormatConfigTests(unittest.TestCase):
    def test_format_config_uses_requested_output_order(self) -> None:
        config = AppConfig(
            app_name="animated-garbanzo",
            environment="development",
            debug_mode=False,
            runtime_checks=True,
        )

        self.assertEqual(
            format_config(config),
            "app name: animated-garbanzo\n\n"
            "environment: development\n\n"
            "debug mode: False\n\n"
            "runtime checks: True",
        )


if __name__ == "__main__":
    unittest.main()
