import unittest


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# REDO
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, curr = result[-1], intervals[i]
            if curr.start <= prev.end:
                prev.end = max(prev.end, curr.end)
            else:
                result.append(curr)
        return result


class Tests(unittest.TestCase):
    def test_merge_overlapping_intervals(self):
        solution = Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
        expected = [[1, 6], [8, 10], [15, 18]]
        for x, y in zip(solution, expected):
            self.assertEqual(x.start, y[0])
            self.assertEqual(x.end, y[1])
