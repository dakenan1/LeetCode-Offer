# -*- coding:utf-8 -*-      #理解return A and B！
class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n>0 and qiusum(n)
        print qiusum(n)
        return self.sum