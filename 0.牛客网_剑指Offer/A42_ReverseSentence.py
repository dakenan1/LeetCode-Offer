# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        string = s.split()
        if len(string) == 0:       #输入的是空格的话，split会删去
            return s
        string.reverse()
        s = ' '.join(string)
        return s