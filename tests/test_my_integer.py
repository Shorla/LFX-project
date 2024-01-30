from unittest.mock import patch
import unittest
import sys
from io import StringIO
from my_integer import get_user_input, multiples

class MyIntegerTests(unittest.TestCase):

    def test_confirmation(self):
        user_input = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
        with patch.object(sys, 'stdin', StringIO(user_input)):
            self.assertEqual(get_user_input(), user_input.strip())

    def test_invalid_input(self):
        user_input = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19'
        with patch.object(sys, 'stdin', StringIO(user_input)):
            self.assertEqual(get_user_input(), user_input.strip())
  
                
if __name__ == '__main__':
    unittest.main()

    

