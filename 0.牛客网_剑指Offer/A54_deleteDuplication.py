# -*- coding:utf-8 -*-             #艰难通过，务必多练习！！！！
# class ListNode:                  #ListNode[0/-1]是什么意思？？？ 新的节点不能为空，因此随便去一个前面有的值作为新起点
#     def __init__(self, x): 
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead, new):     
        # write code here
        #new = ListNode(0)
        if not pHead or not pHead.next:
            return pHead
        p2 = pHead
        flag = 1
        while p2:
            if not p2.next:
                if flag == 1:
                    new.next = p2
                else:
                    pHead.next = p2
                break
            if p2.val == p2.next.val:
                while p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                pHead.next = None
                p2 = p2.next
            else:
                if flag == 1:
                    flag = 0
                    pHead = p2
                    new.next = pHead
                else:
                    pHead.next = p2
                    pHead = pHead.next
                p2 = p2.next
        return new.next


