# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        l = list(ss)
        l.sort()
        res = []
        for i in range(1,len(l)):
            if l[i] != l[j]: 
                l[0],l[i] = l[i],l[0] 
                str1 = [''.join(l)]
                l[0],l[i] = l[i],l[0]
                sum = sum + str1





"""         if not ss:
            return []
        l = list(ss)
        sum = [ss]
        for j in range(len(l)-1):
            for i in range(j+1,len(l)):
                if l[i] != l[j]: 
                    l[j],l[i] = l[i],l[j]
                    str1 = [''.join(l)]
                    l[j],l[i] = l[i],l[j]
                    sum = sum + str1
        sum.sort()
        return sum
 """