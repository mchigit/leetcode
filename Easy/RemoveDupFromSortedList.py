"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        curr = head
        while curr != None and curr.next != None:
            temp = curr.next
            while temp != None and temp.val == curr.val:
                temp = temp.next
            curr.next = temp
            curr = curr.next

        return head