# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        l = []
        if not num:
            return l
        if size == 0:
            return l
        for i in range(len(num)-size+1):
            l.append(max(num[i:i+size]))
        return l