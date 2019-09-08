# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self,listNode):
        # write code here
        if not listNode:
            return[]
        else:
            list = []
            head = listNode
            while head:
                list.insert(0,head.val)    #每次都从0插入，实际上是倒叙了！
                head = head.next
            return list





""" def __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2) """