# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    def mergeKLists(self, lists):
        if not lists: return ''
        if not lists[0]: return ''
        if len(lists) == 1: return lists[0]
        i = 2
        ll = self.mergeTwoLists(lists[0],lists[1])
        while i < len(lists): 
            ll = self.mergeTwoLists(ll, lists[i])
            i += 1
        return ll

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        phead = ListNode(0)
        l3 = ListNode(1)
        if l1.val < l2.val: 
            l3 = l1
            l1 = l1.next
        else: 
            l3 = l2
            l2 = l2.next
        phead.next = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1: 
            l3.next = l1
        elif l2: l3.next = l2
        return phead.next