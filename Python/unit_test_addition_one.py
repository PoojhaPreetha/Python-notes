import unittest
import pylint_addition
class TestAddition(unittest.TestCase):
    def test_two_numbers(self):
        A = 4
        B = 5
        result = pylint_addition.addition(A,B)
        self.assertEqual(result,9)
    def test_mul_numbers(self):
        A = 1
        B = 2
        C = 3
        result = pylint_addition.addition(A,B,C)
        self.assertEqual(result,0)
    def test_list_of_numbers(self):
        l = list(range(1,10))
        result = pylint_addition.addition(l)
        self.assertEqual(result,45)
if __name__ == '__main__':
    unittest.main()
