import unittest


class Solution:
    # @param A : string
    # @return an integer
    # Sliding Window
    def lengthOfLongestSubstring(self, A):
        n = len(A)
        s = set()
        ans, i, j = 0, 0, 0
        while i < n and j < n:
            if A[j] not in s:
                s.add(A[j])
                j += 1
                ans = max(ans, j - i)
            else:
                s.remove(A[i])
                i += 1
        return ans

    # Use hashtable
    def lengthOfLongestSubstringOptimized(self, A):
        m = {}
        ans, i, j = 0, 0, 0
        for j in xrange(len(A)):
            if A[j] in m:
                i = max(m[A[j]], i)
            ans = max(ans, j - i + 1)
            m[A[j]] = j + 1
        return ans


class Tests(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        sol = Solution()
        self.assertEqual(7, sol.lengthOfLongestSubstring('geeksforgeeks'))
        self.assertEqual(3, sol.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, sol.lengthOfLongestSubstring('bbbbb'))
        self.assertEqual(4, sol.lengthOfLongestSubstring('dadbc'))
