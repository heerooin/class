import unittest
from unittest.mock import patch
from src.saver import JSONSaver
from src.vacancies import Vacancies

class TestVacancyClass(unittest.TestCase):
    def test_vacancy_creation(self):
        vacancy = Vacancies("Python Developer", "example.com", "100000-150000", "Experience: 3 years")

        self.assertEqual(vacancy.name, "Python Developer")
        self.assertEqual(vacancy.url, "example.com")
        self.assertEqual(vacancy.salary, '100000-150000')
        self.assertEqual(vacancy.description, "Experience: 3 years")

    def test_vacancy_creation_with_missing_salary(self):
        vacancy = Vacancies("Python Developer", "example.com", None, "Experience: 3 years")

        self.assertEqual(vacancy.salary, 0)

    def test_vacancy_comparison(self):
        vacancy1 = Vacancies("Python Developer", "example1.com", "100000", "Experience: 3 years")
        vacancy2 = Vacancies("Python Developer", "example2.com", "120000", "Experience: 5 years")

        self.assertLess(vacancy1, vacancy2)


class TestJSONSaverClass(unittest.TestCase):
    @patch('builtins.open', create=True)
    def test_add_vacancy(self, mock_open):
        vacancy = Vacancies("Python Developer", "example.com", "100000-150000", "Experience: 3 years")
        json_saver = JSONSaver()

        json_saver.add_vacancy(vacancy)

        mock_open.assert_called_once_with('vacancies.json', 'a')



if __name__ == '__main__':
    unittest.main()