# -*- coding:utf-8 -*-             #单项链表、公共节点的定义
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1 = []
        l2 = []
        if not pHead1 or not pHead2:
            return 
        while pHead1:
            l1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.val in l1:
                return pHead2
            else:
                pHead2 = pHead2.next