import unittest
from collections import Counter


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        counter = Counter(A)
        results = []
        self.permute_helper(counter, [0] * len(A), results, 0)
        return results

    def permute_helper(self, counter, so_far, results, level):
        if level == len(so_far):
            results.append(list(so_far))
            return

        for i in counter:
            if counter[i] == 0:
                continue
            so_far[level] = i
            counter[i] -= 1
            self.permute_helper(counter, so_far, results, level + 1)
            counter[i] += 1


class Tests(unittest.TestCase):
    def test_permute(self):
        self.assertEqual(sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]]), sorted(Solution().permute([1, 1, 2])))
