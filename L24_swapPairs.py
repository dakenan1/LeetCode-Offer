# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
    #def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ph = ListNode(0)
        uph = ph
        ph.next = head.next
        while head and head.next:
            uph.next = head.next
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            uph = head
            head = head.next
        return ph.next