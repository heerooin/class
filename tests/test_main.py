import unittest
from unittest.mock import patch
from io import StringIO
from src.main import user_interaction


class TestMainInteraction(unittest.TestCase):

    @patch('builtins.input', side_effect=["it", "1", "python", "100000"])
    @patch('src.api.HeadHunterAPI.get_vacancies', return_value={'items': []})
    def test_user_interaction_no_vacancies(self, mock_input, mock_get_vacancies):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_interaction()
            self.assertIn("Нет подходящих вакансий", mock_stdout.getvalue())




if __name__ == '__main__':
    unittest.main()
