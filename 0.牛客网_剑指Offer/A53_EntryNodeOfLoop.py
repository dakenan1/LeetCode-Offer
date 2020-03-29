# -*- coding:utf-8 -*-                    #调试未通过
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return
        pHead2 = pHead
        while pHead2 and pHead2.next:
            pHead = pHead.next
            pHead2 = pHead2.next.next
            if pHead2 == pHead:                   #有时候pHead和pHead.val无法区分！
                if pHead.next == pHead2.next:
                    return pHead
                else:
                    continue
        return         

