"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Runtime: 84 ms, faster than 32.86% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode(0)
        answer = result
        while l1 and l2:
            sumNode = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            result.next = sumNode
            result = result.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            result.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            result = result.next

        while l2:
            result.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            result = result.next

        if carry != 0:
            result.next = ListNode(carry)

        return answer.next