import unittest
from unittest.mock import patch
from io import StringIO
import os
import multiply
# from multiply import *


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

    def test_update_score(self):
        # Test that the high score is updated correctly
        correct_count = 10
        wrong_count = 5
        high_score = 8
        wrong_answers = [(2, 2, 4), (3, 3, 9)]
        multiply.update_score(correct_count, wrong_count, high_score, wrong_answers)
        self.assertEqual(multiply.get_high_score(), 10)

    def test_generate_division_question(self):
        # Test that the division question is generated correctly
        num1, num2, quotient = multiply.generate_division_question()
        self.assertEqual(num1 / num2, quotient)

    def test_generate_multiplication_question(self):
        # Test that the multiplication question is generated correctly
        num1, num2, product = multiply.generate_multiplication_question()
        self.assertEqual(num1 * num2, product)

    def test_check_answer(self):
        # Test that the answer is checked correctly
        self.assertEqual(multiply.check_answer(5, 5, int), (True, False))
        self.assertEqual(multiply.check_answer(5, 4, int), (False, False))
        self.assertEqual(multiply.check_answer('invalid', 5, int), (False, True))


if __name__ == '__main__':
    unittest.main()