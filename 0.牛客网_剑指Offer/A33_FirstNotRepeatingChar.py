# -*- coding:utf-8 -*-         #简单哈希表
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        li = map(str,s)
        num = [0]*256
        for i in li:
            num[ord(i)] += 1    
        for j in li:
            if num[ord(j)] == 1:
                return li.index(j)  
        return -1