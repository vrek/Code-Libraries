"""This will test the math helper function library"""
import unittest
from mathhelper import is_prime
"""This is a unit test class"""
class testMathHelper(unittest.TestCase):
    def test_is_prime(self):
        """Tests a the function is_prime is properly calculating prime numbers"""
        self.assertEqual(is_prime(100),False)
        self.assertEqual(is_prime(1),False)
        self.assertEqual(is_prime(0),False)
        self.assertEqual(is_prime(7),True)
        self.assertEqual(is_prime(2),True)


if __name__=='__main__':
    unittest.main()
