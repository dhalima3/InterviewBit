import unittest


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if not A:
            return A
        A = A[::-1]
        A[0] += 1
        carry = 0
        for i, e in enumerate(A):
            A[i] += carry
            carry = A[i] / 10
            A[i] %= 10
        if carry:
            A.append(1)
        A = A[::-1]
        while A[0] == 0:
            del A[0]
        return A


class Tests(unittest.TestCase):
    def test_plus_one(self):
        self.assertEqual([1, 0, 0], Solution().plusOne([9, 9]))
        self.assertEqual([3, 7, 6, 4, 0, 5, 5, 6], Solution().plusOne([0, 3, 7, 6, 4, 0, 5, 5, 5]))
