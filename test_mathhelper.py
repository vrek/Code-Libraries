"""This will test the math helper function library"""
import unittest
from mathhelper import list_primes, is_prime, count_primes
if __name__=='__main__':
    unittest.main()

class TestMathHelper(unittest.TestCase):
    """Unit Test class for Math Helper"""
    def test_is_prime(self):
        """Tests a the function is_prime is properly calculating prime numbers"""
        self.assertEqual(is_prime(100),False)
        self.assertEqual(is_prime(1),False)
        self.assertEqual(is_prime(0),False)
        self.assertEqual(is_prime(7),True)
        self.assertEqual(is_prime(2),True)
        self.assertEqual(is_prime(3),True)
        """Tests that incorrect input data types are correctly handled"""
        self.assertRaises(TypeError, is_prime, True)
        self.assertRaises(TypeError, is_prime, 'five')
        self.assertRaises(TypeError, is_prime, 4+6j)
    def test_list_primes(self):
        """tests functionality of list primes"""
        self.assertEqual(list_primes(3),[2,3,])
        self.assertEqual(list_primes(10),[2,3,5,7,])
        """Tests that incorrect input data types are correctly handled"""
        self.assertRaises(TypeError, is_prime, True)
        self.assertRaises(TypeError, is_prime, 'five')
        self.assertRaises(TypeError, is_prime, 4+6j)
    def test_count_primes(self):
        """tests functionality of count_primes"""
        self.assertEqual(count_primes(0,10), 4)
        self.assertEqual(count_primes(72,174), 20)
