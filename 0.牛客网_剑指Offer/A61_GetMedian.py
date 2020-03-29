# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
        self.len = 0
    def Insert(self, num):
        # write code here
        self.data.append(float(num))
        self.len += 1
    def GetMedian(self,data):
        # write code here
        self.data.sort()
        if self.len == 0:
            return  
        elif self.len%2 == 0:
            return (self.data[self.len/2] + self.data[(self.len/2)-1]) / 2
        else:
            return self.data[self.len/2]