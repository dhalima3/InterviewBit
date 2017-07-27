import re
import unittest


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        l = 0
        first = True
        for c in A[::-1]:
            if c == ' ' and not first:
                break
            if c == ' ':
                continue
            if re.match('[A-Za-z]', c):
                l += 1
                first = False
        return l


class Tests(unittest.TestCase):
    def test_length_of_last_word(self):
        self.assertEqual(5, Solution().lengthOfLastWord("Hello World  "))
