import unittest
import assignment_one
from assignment_one import prime
class Prime_num(unittest.TestCase):
    def test_prime(self):
        A = 5
        r=assignment_one.prime(A)
        self.assertEqual(r,5)
    def test_not_prime(self):
        A=90
        r=assignment_one.prime(A)
        self.assertEqual(r,90)
if __name__ == '__main__':
    unittest.main()
