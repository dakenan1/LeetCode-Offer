# -*- coding:utf-8 -*-
from A65_cutRope import Solution

s = Solution()

print(s.cutRope(3))


""" from A35_GetNumberOfK iport Solution
string = 'NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'
s = Solution()
a = [1,3,3,3,3,4,5]

print s.GetNumberOfK(a,2) """



""" a = [2]        #input
b = '0x1111'
print a[0]
print str(a[0])
print type(a[0])
print type(str(a[0]))
#a,b = map(int,raw_input().split()) """



""" l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','W','Y','Z']
print len(l)
print type(l[0])
print l.index('A') """

""" l = []
r = []
for i in bin(7):
    l.append(i)
l.pop(0)
l.pop(0)
for j in l:
    r.append(j)
l.reverse()    
    if l == r: ans.append('YES')
    else: ans.append('NO')
for k in range(len(ans)):
    print ans[k]  """

""" for i in bin(h):
    l.append(i)
print l
print d.pop(0)
# print ' '.join(str(a[i]) for i in range(2)) """

""" s = Solution()
print s.FindGreatestSumOfSubArray([-4,-3,8,8])  """



""" v = 'a'
v1 = [v]
v2 = v1 * 3
v3 = [v2]
v4 = v3 * 3
v4[0][0] = 'b'
print v4
val=[['a'] * 3] * 3
val[0][0]='b'
print val """




""" push = [1,2,3,4,5]     #A20
pop = [4,3,5,1,2]
print s.IsPopOrder(push, pop) """




""" 
s.push(3)                 # A19
print s.min()
s.push(4)
print s.min()
s.push(2)
print s.min()
s.push(3)
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()
s.push(0)
print s.min() """
""" d.append([1,1,1,1])   pop and push
print d
print d.pop(0)
print d """

"""         #聚类中心初始化
#ranges = [ (min([row[i] for row in rows]),max([row[i] for row in rows])) for i in range(len(rows[0]))]
c = []
d = []
ranges = []
for i in range(len(rows[0])):
    c = []
    for row in rows:
        c.append(row[i])
    ranges.append((min(c),max(c)))  
print ranges

re = []
for j in range(3):
    for i in range(len(rows[0])):
        re = random.random()*(ranges[i][1]-ranges[i][0]) + ranges[i][0]
        print re """
    

""" class ListNode(object):          # train 15
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "%r" % self.val
class SingleLinkList(object):
    
    def __init__(self):
        self._head = None
if __name__ == '__main__':
    # 创建链表
    link_list = SingleLinkList()
    # 创建结点
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    # 将结点添加到链表
    link_list._head = node1
    # 将第一个结点的next指针指向下一结点
    node1.next = node2
    node2.next = node3

    link_list2 = SingleLinkList()
    node21 = ListNode(2)
    node22 = ListNode(4)
    node23 = ListNode(6)
    # 将结点添加到链表
    link_list2._head = node21
    # 将第一个结点的next指针指向下一结点
    node21.next = node22
    node22.next = node23
    s = Solution()
    re = s.Merge(link_list._head,link_list2._head)
    print re """


"""     # 访问链表
    print(link_list._head.val)  # 访问第一个结点数据
    print(link_list._head.next.val)  # 访问第二个结点数据
    print(link_list._head.next.next.val) #第三个！
    print(link_list2._head.val)  # 访问第一个结点数据
    print(link_list2._head.next.val)  # 访问第二个结点数据
    print(link_list2._head.next.next.val) #第三个！ """


""" 
 

s = Solution()
print s.reOrderArray([]) """


"""print s.NumberOf1(-8) """

""" n = 7 
num = [0,1]
for i in range(2,n):
    num.append(num[i-1] + num[i-2])
print num[n-1] """


""" for i in range(2,8):
    print i """

""" 

print(s.minNumberInRotateArray(q))

 """

""" print(Quick_array2(c)) """ 

""" 
b = [9,8,7,6,4,2,1,0]    #bubble sort test

c = []a

print(Bubble_array(c)) 
"""



""" class LNode(object):                #train4
    #结点初始化函数, p 即模拟所存放的下一个结点的地址
    #为了方便传参, 设置 p 的默认值为 0 
    def __init__(self, data, p=0):
        self.data = data
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = None
    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = LNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            print(node)
            p.next = node
            p = p.next
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, LinkList):
        # write code here
        l = []
        header = LinkList
        while header:
            l.insert(0, header.head)
            header = header.next
        print(l)
data = [1,7,3,4,5]

result = LinkList()
result.initList(data)

s = Solution()
s.printListFromTailToHead(result)  """          


""" 
class Node:
    def __init__(self,cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.cargo)
print (Node("text"))
 """


""" a = 'We Are Happy'
b = ''

res = ''
for ele in b:
    if ele.strip():
        res += ele
    else:
        res += '%20'
    print '0'
print res """


""" if not b.strip(''):
    print('yes')

print(b.strip()) """


""" for i in a:
    if i == ' '

    print(i) """
""" str = b.split(' ')
print(str)
b = '%20'.join(str)
print(b)
c = []
print('%20'.join(c)) """
""" s = Solution()                             #train2
print(s.replacespace(b)) """


""" #import train1                             #train1
a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]  #测试编码
target = 16
s= Solution()
print(s.Find(target,a)) """

""" b = len(a[0])
c = len(a)
print(b,c) """
"""print(a.isdigit())
print("测试编码") """

""" for i in range(18):
    print(i)
 """