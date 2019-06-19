"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


Draw it out for visualization of solution
"""



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = ListNode(0)
        temp.next = head
        curr = temp

        while curr.next != None and curr.next.next != None:
            left = curr.next
            right = curr.next.next
            left.next = right.next
            right.next = left
            curr.next = right
            curr = curr.next.next

        return temp.next