# -*- coding:utf-8 -*-
class Solution:             #没有实现书中的异或思路
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return None
        if len(array) == 1:
            return array[0]
        re = []
        i = 0
        while array:
            a = array[0]
            array.pop(0)
            if a in array:
                array.remove(a)
            else:
                re.append(a)
        return re