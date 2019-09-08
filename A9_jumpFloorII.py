# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        n = number
        f = 1
        for i in range(n-1):
            f = f * 2
        return f