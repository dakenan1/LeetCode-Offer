# -*- coding:utf-8 -*-       #认真理解好求加法的原理以及不进位加法以及仅计算进位的位运算匹配
class Solution: 
    def Add(self, a, b):           
        while(b): 
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)
