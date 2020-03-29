# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        n = number
        if n == 0: return 0
        elif n == 1: return 1
        else:
            num = [1,1]                    #修改了第二阶的次数，初始化
            for i in range(2,n+1):
                num.append(num[i-1] + num[i-2])
        return num[n]