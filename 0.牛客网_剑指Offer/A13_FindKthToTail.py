# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def FindKthToTail(self, head, k):
        # write code here
        list = []
        if not head:
            return 
        while head:
            list.append(head)
            head = head.next
        if len(list)<k or k<1:
            return
        return list[-k]