import unittest
from maxSubString import maxSString


class Testdemo(unittest.TestCase):
    #test maxSubString.py

    @classmethod
    def setUpClass(cls):
        print("Prepare for unittest...")

    @classmethod
    def tearDownClass(cls) :
        print("Thankyo for testing...")

    def test_msstring(self):
        self.assertEqual(111, maxSString("-32 -10 33 -23 32 -12 41 -12 1 3 5 -98 70 -21 10 -9 61"))
        self.assertRaises(ValueError, maxSString, "-32, -10, 33, -23, 32, -12, 41, -12, 1, 3, 5, -98, 70, -21, 10, -9, 61")


if __name__ == '__main__':
    unittest.main(verbosity=1)
