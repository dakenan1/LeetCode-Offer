# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) <= 1:
            return []
        if array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array)-1
        re = []
        result = []
        while start < end:
            if array[start] + array[end] < tsum:
                start += 1
            elif array[start] + array[end] > tsum:
                end -= 1
            else:
                re.append(array[start])
                re.append(array[end])
                start += 1
                end -= 1
        if not re:
            return []
        elif len(re) == 2:
            return re
        else:
            for i in range(len(re)-1):
                result.append(re[i]*re[i+1])
                i += 1
            ind = result.index(min(result))
            return re[2*ind:2*ind+2]