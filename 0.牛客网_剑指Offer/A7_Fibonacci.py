# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0: return 0
        elif n == 1: return 1
        else:
            num = [0,1]
            for i in range(2,n+1):
                num.append(num[i-1] + num[i-2])
        return num[n]
    




"""         if n == 0: return 0    #递归，计算量极大
        elif n == 1: return 1
        else:
            num = self.Fibonacci(n-1) + self.Fibonacci(n-2)
            return num """