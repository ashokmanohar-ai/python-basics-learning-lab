import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CourseStructureTests(unittest.TestCase):
    def test_all_required_topics_appear_in_lessons(self):
        content = " ".join(
            path.read_text(encoding="utf-8").lower()
            for path in (ROOT / "notebooks").glob("*.ipynb")
        )
        topics = [
            "variables", "data types", "operators", "conditional", "loops", "functions",
            "lists", "tuples", "dictionaries", "sets", "exception", "file handling",
            "object-oriented programming",
        ]
        for topic in topics:
            with self.subTest(topic=topic):
                self.assertIn(topic, content)

    def test_notebooks_use_python_3_kernel(self):
        for path in ROOT.rglob("*.ipynb"):
            with self.subTest(path=path.relative_to(ROOT)):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                kernel = notebook["metadata"]["kernelspec"]["name"]
                self.assertEqual(kernel, "python3")

    def test_projects_include_stretch_goals(self):
        for path in (ROOT / "projects").glob("*.ipynb"):
            with self.subTest(path=path.name):
                self.assertIn("Stretch goals", path.read_text(encoding="utf-8"))

    def test_sample_data_is_present(self):
        self.assertTrue((ROOT / "data" / "sample_expenses.csv").is_file())
        self.assertTrue((ROOT / "data" / "reading_list.txt").is_file())


if __name__ == "__main__":
    unittest.main()
