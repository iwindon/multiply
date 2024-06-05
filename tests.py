import unittest
from unittest.mock import patch
from io import StringIO
import os
import multiply

class TestMultiply(unittest.TestCase):
    @patch('builtins.input', return_value='5')
    def test_display_times_tables(self, input):
        expected_output = '\n'.join([f"5 * {i} = {5 * i}" for i in range(1, 11)]) + '\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            multiply.display_times_tables()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_update_score(self, mock_open):
        multiply.update_score(10, 5, 8, [])
        mock_open.assert_called_once_with('high_score.txt', 'w')

    @patch('builtins.input', return_value='easy')
    def test_set_difficulty(self, input):
        self.assertEqual(multiply.set_difficulty(), 30)

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='10')
    def test_get_high_score(self, mock_open):
        self.assertEqual(multiply.get_high_score(), 10)

    # Add more tests for division_practice, multiplication_practice, and the main program

if __name__ == '__main__':
    unittest.main()