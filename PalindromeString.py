import string
import unittest


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = ''.join(A.lower().split()).translate(None, string.punctuation)
        return 1 if A == A[::-1] else 0


class Tests(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(1, Solution().isPalindrome('A man, a plan, a canal: Panama'))
        self.assertEqual(0, Solution().isPalindrome('race a car'))
