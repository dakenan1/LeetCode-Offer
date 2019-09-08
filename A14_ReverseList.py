# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:                     #画链表图变化理解！
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:                    #last、pHead.next分别代表pHead上下节点
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last