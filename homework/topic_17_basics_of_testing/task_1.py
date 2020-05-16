import unittest
import homework.topic_10_functions_as_first_class_objects.task_1


class HumanTestCase(unittest.TestCase):

    def setUp(self):
        self.human = homework.topic_10_functions_as_first_class_objects.task_1.Human('oleh', 22, 'ukraine', 'vinnytsia')


if __name__ == '__main__':
    unittest.main()
