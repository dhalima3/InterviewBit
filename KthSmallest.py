import heapq
import unittest


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    # Create min heap, and extract min k times
    def kthsmallest(self, A, k):
        smallest = None
        A = list(A)
        heapq.heapify(A)
        for i in xrange(k):
            smallest = heapq.heappop(A)
        return smallest


class Tests(unittest.TestCase):
    def test_check_subtree(self):
        sol = Solution()
        self.assertEqual(2, sol.kthsmallest([2, 1, 4, 3, 2], 3))
        self.assertEqual(3, sol.kthsmallest([2, 1, 4, 3, 2], 4))
