# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

        # while l1.next and l2.next:
        #     if l1.val < l2.val:
        #         if l1.next.val >= l2.val:
        #             tmp = l1.next 
        #             l1.next = l2
        #             tmp2 = l2.next
        #             l2.next = tmp
        #             l2 = tmp2
        #             l1 = tmp
        #         else:                  
        #             l1 = l1.next
        #     else:
        #         l2 = l2.next    

        # if l1.next: 
        #     while l1.val < l2.val:
        #         l1 = l1.next
        #     tmp = l1.next
        #     l2.next = tmp
        #     l1.next = l2  
        # elif not l1.next and not l2.next: 
        #     if l1.val <= l2.val:
        #         l1.next = l2
        #     else:
        # return phead.next
            
