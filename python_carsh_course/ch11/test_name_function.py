import unittest
from python_carsh_course.ch11.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jack', 'chen')
        self.assertEqual(formatted_name, 'Jack Chen')


unittest.main()
