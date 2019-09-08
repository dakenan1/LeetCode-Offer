# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:                     #未完成
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        mergeHead = ListNode(90)
        p = mergeHead                             #p的意义在哪？
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                mergeHead.next = pHead2
                pHead2 = pHead2.next
            else:
                mergeHead.next = pHead1
                pHead1 = pHead1.next
                  
            mergeHead = mergeHead.next
        if pHead1:
            mergeHead.next = pHead1
        elif pHead2:
            mergeHead.next = pHead2
        return p.next



"""         if not pHead1:                  #将链表二并入链表一，未完成
            return pHead2
        if not pHead2:
            return pHead1
        while pHead2:
            if not pHead1.next:
                pHead1.next = pHead2
                return pHead1
            if pHead1.val >= pHead2.val: 
                tmp1 = pHead1
                tmp2 = pHead2   
                pHead2 = pHead2.next              
                pHead1 = tmp2
                pHead1.next = tmp1
            else:
                pHead1 = pHead1.next
        return pHead1.next """




            

