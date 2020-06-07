# encoding: utf-8

"""
date: 2020/03/01/17/39

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        fast = slow = head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


