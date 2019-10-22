# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        r = ListNode(0)                            # 设立值为0的节点赋予r，该值无所谓
        re = r                                     # 设立真正遍历的节点，原来的r用于直接返回re的头部 == r.next
        sum = 0
        flag = 0
        while l1 or l2:
            x= l1.val if l1 else 0                 # 下一节点有可能为None，因此不能直接调用
            y= l2.val if l2 else 0               
            sum = x + y + flag
            if sum >= 10:
                flag = 1
                sum -= 10
            else:
                flag = 0
            re.next = ListNode(sum)
            re = re.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if flag != 0:
            re.next = ListNode(flag)
            re = re.next
        return r.next
