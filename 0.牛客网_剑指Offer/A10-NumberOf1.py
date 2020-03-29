# -*- coding:utf-8 -*-
class Solution:               #未通过
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff   #负数变正数，四个字节
        while n:
            count += 1
            n = (n - 1) & n
        return count
"""         lolo = []
        if not n:
            return
        if n == 0:
            return 0
        while n >= 1:
            b = n%2
            lolo.append(b) 
            n = n/2
        return lolo[::-1] """