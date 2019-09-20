# -*- coding:utf-8 -*-      #核心公式！！！！
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0:
            return -1
        l = [i for i in range(n)]
        while len(l) > 1:
            long = len(l)
            local = m-((m/long))*long-1
            l.pop(local)
            if local < 0:
                local += long 
            l = l[local:] + l[:local]
        return l[0]    