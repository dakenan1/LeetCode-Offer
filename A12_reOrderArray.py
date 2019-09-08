# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        l = []
        r = []
        if not array: return []
        for i in range(len(array)):
            if array[i] % 2 ==0: r.append(array[i])
            else: l.append(array[i])
        return l + r