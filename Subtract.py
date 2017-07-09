import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def subtract(self, A):
        if not A or not A.next:
            return A
        curr = A
        mid = A
        orig = None
        # Find midpoint
        while curr and curr.next:
            orig = mid
            mid = mid.next
            curr = curr.next.next
        orig.next = None

        # Reverse second half of list
        curr = mid
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Subtract first node's value from last node's
        curr = A
        end = prev
        while curr:
            curr.val = prev.val - curr.val
            curr = curr.next
            prev = prev.next

        # Reconstructing the second half of list
        prev = None
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp

        orig.next = prev
        return A


class Tests(unittest.TestCase):
    def create_ll(self, l):
        if len(l) < 1:
            return None
        head = ListNode(l[0])
        temp = head
        for e in l[1:]:
            next = ListNode(e)
            temp.next = next
            temp = temp.next
        return head

    def test_check_subtree(self):
        sol = Solution()
        answer = sol.subtract(self.create_ll([1, 2, 3, 4, 5]))
        expected = [4, 2, 3, 4, 5]
        index = 0
        while answer:
            self.assertEqual(expected[index], answer.val)
            index += 1
            answer = answer.next
