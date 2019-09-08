# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        base = float(base)
        if base == 0 and exponent == 0: return
        if base == 0: return 0
        be = 1
        if exponent == 0 : return 1
        elif exponent > 0:
            for i in range(exponent):
                be = be * base
            return be
        else: 
            return (1/base)**(-exponent)
            