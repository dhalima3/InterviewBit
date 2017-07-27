# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        head = ans = ListNode(0)
        carry = 0
        while A and B:
            ans.next = ListNode((A.val + B.val + carry) % 10)
            carry = 1 if A.val + B.val + carry >= 10 else 0
            A = A.next
            B = B.next
            ans = ans.next
        while A:
            ans.next = ListNode((A.val + carry) % 10)
            carry = 1 if A.val + carry >= 10 else 0
            A = A.next
            ans = ans.next
        while B:
            ans.next = ListNode((B.val + carry) % 10)
            carry = 1 if B.val + carry >= 10 else 0
            B = B.next
            ans = ans.next
        if carry:
            ans.next = ListNode(carry)
        return head.next
