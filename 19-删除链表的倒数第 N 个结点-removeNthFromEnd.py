# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 使用字典保存链表节点
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        pre = ListNode(0, head)
        node =  pre
        idx = 0
        node_dic = {}
        while node:
            node_dic[idx] = node
            idx += 1
            node = node.next
        node_dic[idx - n - 1].next = node_dic[idx - n].next
        return pre.next
    
    # 使用快慢指针
    def removeNthFromEnd1(self, head: [ListNode], n: int) -> [ListNode]:
        pre = ListNode(0, head)   # 伪头节点
        fast = pre    # 快指针，领先慢指针n+1个节点，初始为pre
        for _ in range(n + 1):
            fast = fast.next   # 后移快指针，使得快指针领先慢指针n+1个节点
        slow = pre    # 慢指针，用于定位要删除节点的前一个节点
        # 当快指针到达链表末尾时，慢指针到达要删除节点的前一个节点
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # 将删除节点的前一个节点的next指向删除节点的后一个节点，即删除了节点
        return pre.next 

# 作者：画图小匠
# 链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/2411535/javapython3ckuai-man-zhi-zhen-jian-ge-we-gjmb/
