# -*- coding:utf-8 -*-            #经典递归法！值得表扬！！
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        length = len(data)
        if length == 0:
            return 0
        if length == 1:
            if data[0] == k: return 1
            else: return 0
        if data[length-1] < data[0]: data.reverse()
        if data[0]>k: return 0       
        elif data[length-1]<k: return 0
        
        mid = length/2
        if data[mid] == k:
            return self.GetNumberOfK(data[mid:],k) + self.GetNumberOfK(data[:mid],k)
        elif data[mid] > k:
            return self.GetNumberOfK(data[:mid],k)
        else: 
            return self.GetNumberOfK(data[mid+1:],k)
