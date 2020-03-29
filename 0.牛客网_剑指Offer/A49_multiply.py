# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return A
        elif len(A) == 1:
            return [0]
        n = len(A)
        B = [1] * n
        mid1 = 1 
        mid2 = 1
        for i in range(n-1):                #本身不乘的标签改变
            mid1 *= A[n-i-1]
            B[n-i-1-1] = mid1
        for j in range(1,n):
            mid2 *= A[j-1]
            B[j] *= mid2
        return B