# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        def camp(a,b):
            if int(str(a)+str(b))<int(str(b)+str(a)):
                return -1
            elif int(str(a)+str(b))>int(str(b)+str(a)):
                return 1
            else:
                return 0
        tmpNumbers = sorted(numbers,cmp=camp)
        return int(''.join(str(i) for i in tmpNumbers))

