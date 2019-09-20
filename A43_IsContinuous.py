# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5: return False
        numbers.sort()
        flag = 0
        while numbers:
            if numbers[0] == 0:
                flag += 1
                numbers.pop(0)
            else:
                break
        if not numbers: return True
        base = numbers[0]
        times = 0
        for j in range(1,len(numbers)):
            if numbers[j] == base: return False
            elif numbers[j] == base + 1: base += 1
            else: 
                times += numbers[j]-base-1
                base = numbers[j]
            if times > flag: return False
        if times <= flag: return True
        else: return False
