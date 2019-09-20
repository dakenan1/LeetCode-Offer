# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers: 
            return False
        while numbers:
            num = numbers.pop(0)
            if num in numbers:
                duplication[0] = num
                return True
        return False