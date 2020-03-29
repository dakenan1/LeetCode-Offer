# -*- coding:utf-8 -*-
class Solution:
    def Find(self, target, array): 
        a = len(array)
        b = len(array[0])
        flag = False
        x = b-1
        y = 0
        for num in range(a+b-2):
            if array[y][x] == target:
                flag = True
                break
            elif array[y][x] < target:
                y = y + 1
                flag = False    
            elif array[y][x] > target:
                x = x - 1
                flag = False
            elif x < 0 or y > a-1:    
                flag = False
                break
        return flag