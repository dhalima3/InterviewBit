import unittest


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        largest = 1
        for num in A[::-1]:
            curr = roman_to_int[num]
            if curr < largest:
                ans -= curr
            else:
                ans += curr
            largest = max(largest, curr)
        return ans

class Tests(unittest.TestCase):
    def test_roman_to_integer(self):
        self.assertEqual(1954, Solution().romanToInt('MCMLIV'))
