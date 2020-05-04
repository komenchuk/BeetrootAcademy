import unittest
import homework.topic_10_functions_as_first_class_objects.task_1


class MyTestCase(unittest.TestCase):

    def testing_name(self):
        nm = homework.topic_10_functions_as_first_class_objects.task_1.Human.__init__('oleh', 22, 'ukraine',
                                                                                      'vinnytsia')
        self.assertEqual(nm, ('Oleh', 22, 'Ukraine', 'Vinnytsia'))


if __name__ == '__main__':
    unittest.main()
