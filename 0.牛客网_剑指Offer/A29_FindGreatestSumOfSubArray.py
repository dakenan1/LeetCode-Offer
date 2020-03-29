# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):   #O(n*n)
        # write code here
        if not array:
            return None
        if len(array) == 1:
            return array
        max = array[0]
        for start in range(len(array)):
            sum = 0
            for i in range(start,len(array)):
                sum = sum + array[i]
                if sum > max:
                    max = sum
                if sum < 0:
                    break
        return max 

""" # -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):    #O(n+n)
        # write code here
        # 考虑特殊情况，数组的长度为0
        # 算法的时间复杂度为o(n)
        if len(array)<=0:
            return []
        temp_sum = 0
        list_sum = []
        for i in array:
            temp_sum = temp_sum + i
            list_sum.append(temp_sum)
            if temp_sum > 0:
                continue
            else:
                temp_sum = 0
        return max(list_sum) """