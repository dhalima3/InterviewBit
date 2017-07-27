import unittest


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        if not A:
            return A
        A.sort()
        for i in xrange(1, len(A), 2):
            A[i - 1], A[i] = A[i], A[i - 1]
        return A


class Tests(unittest.TestCase):
    def test_wave_array(self):
        self.assertEqual([2, 1, 4, 3], Solution().wave([1, 2, 3, 4]))
        self.assertEqual([2, 1, 3], Solution().wave([1, 2, 3]))
