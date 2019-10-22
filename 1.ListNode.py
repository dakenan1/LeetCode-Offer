# -*- coding:utf-8 -*-
#from L2_addTwoNumbers import Solution
class ListNode(object):          
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "%r" % self.val
class SingleLinkList(object):
    def __init__(self):
        self._head = None
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        r = ListNode(0)
        re = r
        sum = 0
        flag = 0
        while l1 or l2:
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0               
            sum = x + y + flag
            if sum >= 10:
                flag = 1
                sum -= 10
            else:
                flag = 0
            re.next = ListNode(sum)
            re = re.next
            if(l1!=None): l1 = l1.next
            if(l2!=None): l2 = l2.next
        if flag != 0:
            re.next = ListNode(flag)
            re = re.next
        return r.next
if __name__ == '__main__':
    # 创建链表
    link_list = SingleLinkList()
    # 创建结点
    num_list = [2,4,3]
    node_list = []
    for i in num_list:
        node_list.append(ListNode(i))
    # 将结点添加到链表
    link_list._head = node_list[0]
    for j in range(len(num_list)-1):      # 将第一个结点的next指针指向下一结点
        node_list[j].next = node_list[j+1]
    node_list[-1].next = None
    
    # 创建链表
    link_list1 = SingleLinkList()
    # 创建结点
    num_list = [5,6,4]
    node_list = []
    for i in num_list:
        node_list.append(ListNode(i))
    # 将结点添加到链表
    link_list1._head = node_list[0]
    for j in range(len(num_list)-1):      # 将第一个结点的next指针指向下一结点
        node_list[j].next = node_list[j+1]
    node_list[-1].next = None

    new = ListNode(0)
    s = Solution()
    re = s.addTwoNumbers(link_list._head, link_list1._head)
    print(re)

""" 
    print(link_list._head.val)  # 访问第一个结点数据
    print(link_list._head.next.val)  # 访问第二个结点数据
    print(link_list._head.next.next.val) #第三个！   """
