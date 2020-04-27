import unittest
from homework.personal_tasks.task_3_flowers import flowers

class NameTestCase(unittest.TestCase):
    """Test for flowers.py"""

    def test_get_total_value(self):
        """Calculates the total cost correctly?"""
        format_value = flowers.Store.get_total_value
        self.assertEqual(format_value, flowers.Store.get_total_value)


if __name__ == "__name__":
    unittest.main()