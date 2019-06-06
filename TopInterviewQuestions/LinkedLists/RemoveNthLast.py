"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Solution:

have 2 pointers, a slow one and a faster one. Faster one is n steps ahead of slower one.
 When faster one is at the end, slow pointer.next is the element we want to delete

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_pointer, fast_pointer = head, head
        for _ in range(n):
            fast_pointer = fast_pointer.next

        if fast_pointer == None:
            # if linked list only has 1 element, in this case fast = None
            head = head.next
            return head

        while (fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        # at this point, slow_pointer.next is the element we want to remove

        slow_pointer.next = slow_pointer.next.next

        return head