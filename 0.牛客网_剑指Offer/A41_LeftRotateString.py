# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        string = map(str,s)
        if n >= len(s):
            n = n%len(s)
        re = []
        for i in range(n):
            re.append(string.pop(0))
        s = "".join(string + re)
        return s