"""Module to test the functions in the multiply.py file."""
import unittest
from unittest.mock import patch
from io import StringIO
import multiply



class TestMultiply(unittest.TestCase):
    """
    Class to test the functions in the multiply.py file.
    """
    def test_update_score(self):
        """
        Test that the high score is updated correctly.
        """
        # Test that the high score is updated correctly
        correct_count = 10
        wrong_count = 5
        high_score = 8
        operation_symbol = '*'
        wrong_answers = [(2, 2, 4), (3, 3, 9)]
        multiply.update_score(correct_count, wrong_count, high_score, wrong_answers, operation_symbol)
        self.assertEqual(multiply.get_high_score(), 10)

    def test_generate_division_question(self):
        """
        Test that the division question is generated correctly.
        """
        # Test that the division question is generated correctly
        num1, num2, quotient = multiply.generate_division_question()
        self.assertEqual(num1 / num2, quotient)

    def test_generate_multiplication_question(self):
        """
        Test that the multiplication question is generated correctly.
        """
        # Test that the multiplication question is generated correctly
        num1, num2, product = multiply.generate_multiplication_question()
        self.assertEqual(num1 * num2, product)

    def test_check_answer(self):
        """
        Test that the answer is checked correctly.
        """
        # Test that the answer is checked correctly
        self.assertEqual(multiply.check_answer(5, 5, int), (True, False))
        self.assertEqual(multiply.check_answer(5, 4, int), (False, False))
        self.assertEqual(multiply.check_answer('invalid', 5, int), (False, True))


if __name__ == '__main__':
    unittest.main()
# End-of-file (EOF)
