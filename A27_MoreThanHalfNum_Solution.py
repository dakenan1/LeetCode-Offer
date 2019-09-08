# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        lens = len(numbers)
        if lens == 1:
            return numbers[0]
        numbers.sort()
        target = numbers[lens/2]
        index = 0
        end = 0
        for i in range(lens):
            if target == numbers[i]:
                index = i
                break
        for j in range(lens/2,lens):
            if target != numbers[j]:
                end = j
                break
        if end-index > lens/2:
            return target
        else:
            return 0