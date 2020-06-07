# encoding: utf-8

"""
date: 2020/03/01/17/36

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        cur, pre = head, None
        while (cur):
            cur.next, pre, cur = pre, cur, cur.next
        return pre
