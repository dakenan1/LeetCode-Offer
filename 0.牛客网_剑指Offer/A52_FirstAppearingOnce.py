# -*- coding:utf-8 -*-
class Solution:                #输入为字符流，及每次输入一个字符，系统保存并判断一个出现一次的字母
    # 返回对应char
    def __init__(self):
        self.s=""
        self.l = [0] * 256
    def FirstAppearingOnce(self):
        # write code here
        if not self.s:
            return '#'
        for i in self.s:
            if self.l[ord(i)] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        self.l[ord(char)] += 1
        return self.FirstAppearingOnce()