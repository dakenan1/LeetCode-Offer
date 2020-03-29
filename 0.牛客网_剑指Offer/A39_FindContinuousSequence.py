# -*- coding:utf-8 -*-                   #遍历区间依然需要优化
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 2:
            return []
        re = []
        start = 1
        end = 2
        flag = 1
        while start <= tsum/(flag+1):
            if sum(range(start,end+1)) < tsum:
                start += 1
                end += 1
            elif sum(range(start,end+1)) > tsum:  
                flag += 1
                start = 1
                end = start + flag
            elif sum(range(start,end+1)) == tsum:
                re.append(range(start,end+1))
                flag += 1
                start = 1
                end = start + flag
        re.reverse()  
        return re         