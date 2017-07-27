# Definition for singly-linked list.
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        less_than_tail = None
        greater_than_tail = None
        less_than_head = None
        greater_than_head = None
        curr = A
        while curr:
            if curr.val < B:
                if less_than_tail is None:
                    less_than_tail = curr
                    less_than_head = less_than_tail
                else:
                    less_than_tail.next = curr
                    less_than_tail = curr
            else:
                if greater_than_tail is None:
                    greater_than_tail = curr
                    greater_than_head = greater_than_tail
                else:
                    greater_than_tail.next = curr
                    greater_than_tail = curr
            curr = curr.next
        if less_than_tail:
            less_than_tail.next = None
        if greater_than_tail:
            greater_than_tail.next = None

        if not less_than_head:
            return greater_than_head

        if not greater_than_head:
            return less_than_head

        less_than_tail.next = greater_than_head
        return less_than_head


class Tests(unittest.TestCase):
    def test_partitionlist(self):
        sol = Solution()
        five_node = ListNode(31)
        four_node = ListNode(463)
        four_node.next = five_node
        three_node = ListNode(183)
        three_node.next = four_node
        two_node = ListNode(384)
        two_node.next = three_node
        # one_node = ListNode(1)
        # one_node.next = two_node

        end = ListNode(463)
        a = ListNode(183)
        a.next = end
        b = ListNode(384)
        b.next = a
        c = ListNode(31)
        c.next = b

        self.assertEqual(c, sol.partition(two_node, 77))

