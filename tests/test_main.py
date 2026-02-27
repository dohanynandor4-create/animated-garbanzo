import unittest

from src.main import describe_project


class DescribeProjectTests(unittest.TestCase):
    def test_describe_project_returns_expected_message(self) -> None:
        self.assertEqual(
            describe_project(),
            "animated-garbanzo is ready for initial development.",
        )


if __name__ == "__main__":
    unittest.main()
