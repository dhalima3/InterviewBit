import unittest


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A < 1:
            return []
        matrix = [[0 for i in xrange(A * 2 - 1)] for j in xrange(A * 2 - 1)]
        start = A * 2 - 1
        offset = 0

        for i in xrange(A, 1, -1):
            # top row
            for j in xrange(start):
                matrix[offset][j + offset] = i
            # bottom row
            for j in xrange(start):
                matrix[start - 1 + offset][j + offset] = i
            # left column
            for j in xrange(start):
                matrix[j + offset][offset] = i
            # right column
            for j in xrange(start):
                matrix[j + offset][start - 1 + offset] = i
            offset += 1
            start -= 2
        matrix[A-1][A-1] = 1
        return matrix


class Tests(unittest.TestCase):
    def test_check_subtree(self):
        sol = Solution()
        expected_4 = [[4, 4, 4, 4, 4, 4, 4],
                      [4, 3, 3, 3, 3, 3, 4],
                      [4, 3, 2, 2, 2, 3, 4],
                      [4, 3, 2, 1, 2, 3, 4],
                      [4, 3, 2, 2, 2, 3, 4],
                      [4, 3, 3, 3, 3, 3, 4],
                      [4, 4, 4, 4, 4, 4, 4]]
        self.assertEqual(expected_4, sol.prettyPrint(4))
        expected_3 = [[3, 3, 3, 3, 3],
                      [3, 2, 2, 2, 3],
                      [3, 2, 1, 2, 3],
                      [3, 2, 2, 2, 3],
                      [3, 3, 3, 3, 3]]
        self.assertEqual(expected_3, sol.prettyPrint(3))
