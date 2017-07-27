import unittest


# Implement KMP algorithm
class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle or not haystack:
            return -1
        n = 0
        h = 0
        while h < len(haystack):
            if n == len(needle):
                return h - len(needle)
            if haystack[h] == needle[n]:
                n += 1
            else:
                h -= n
                n = 0
            h += 1
        if n == len(needle):
            return h - len(needle)
        return -1


class Tests(unittest.TestCase):
    def test_str_str(self):
        self.assertEqual(4, Solution().strStr('softness', 'ness'))
        self.assertEqual(-1, Solution().strStr('babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba',
                                               'bababbbbbbabbbaabbaaabbbaababa'))
        self.assertEqual(48, Solution().strStr('bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba', 'babaaa'))
