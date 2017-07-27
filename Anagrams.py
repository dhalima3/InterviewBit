import unittest
from collections import defaultdict


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    # Sort each string and keep track of indexes in hash table
    # Time Complexity: O(k(nlogn)) + O(n) where k is length of A
    # Space Complexity: O(k) where k is lengh of A
    def anagrams(self, A):
        A = list(A)
        m = defaultdict(list)
        ans = []
        for i, s in enumerate(A):
            A[i] = ''.join(sorted(s))
            m[A[i]].append(i+1)
        encountered = set()
        for s in A:
            if s not in encountered:
                ans.append(m[s])
                encountered.add(s)
        return ans


class Tests(unittest.TestCase):
    def test_anagrams(self):
        sol = Solution()
        self.assertEqual([[1, 4], [2, 3]], sol.anagrams(['cat', 'dog', 'god', 'tca']))
