# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd(self, head, n):
        if (not head) or (not head.next):
            return None
        p = ListNode(0)
        q = p
        p.next = head
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            p = p.next
        s = p
        tmp = s.next.next
        p.next = tmp
        return q.next
