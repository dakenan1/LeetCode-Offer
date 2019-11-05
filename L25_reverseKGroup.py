# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:       #血妈炸裂！如何处理两个循环中的交接点！！
    #def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    def reverseKGroup(self, head, k):
        if not head or not head.next or k<2: return head
        pre = ListNode(0)
        kh = head
        endh = head
        pre.next = head
        for i in range(k-1):
            kh = kh.next
            if not kh:
                return pre.next  
        pre.next = kh                               # 为了不丢失哑节点只能第一层循环单独处理
        last = kh.next
        head = self.reverse(head, last, k)
        while head:
            kh = head
            for i in range(k-1):
                kh = kh.next
                if not kh:
                    return pre.next                                
            last = kh.next
            endh.next = kh                         # endh作为每层循环的最后一个节点
            endh = head
            head = self.reverse(head, last, k)
        return pre.next
    def reverse(self, head, last, k): 
        for j in range(k):
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        return head

