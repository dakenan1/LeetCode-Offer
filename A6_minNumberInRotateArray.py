# -*- coding:utf-8 -*-                                 
class Solution:                           #failure
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        ar = rotateArray
        if len(ar) == 2:
            if ar[0] >= ar[1]: return ar[1] 
            else: return ar[0]
        elif len(ar) == 1: return ar[0] 
        elif len(ar)== 0: return 0 
        l = 0
        r = len(ar) - 1
        mid = (l+r)//2
        if ar[mid] == ar[0] and ar[mid] == ar[r]:
            for i in range(r+1):
                if ar[i] > ar[i+1]: return ar[i+1]
            return ar[r]
        elif ar[mid] <= ar[r]: ar = ar[:mid]
        elif ar[mid] >= ar[0]: ar = ar[mid:]
        
        s = self.minNumberInRotateArray(ar)
        return s

""" class Solution:
    def minNumberInRotateArray(self, rotateArray):
        low=0
        high=len(rotateArray)-1
        mid=(low+high)/2
        while low<high:
            if rotateArray[mid-1]>rotateArray[mid] and rotateArray[mid+1]>rotateArray[mid]:
                print(rotateArray[mid])
                return rotateArray[mid]
            elif rotateArray[mid]>rotateArray[high]:
                low=mid+1
                mid=(low+high)/2
            elif rotateArray[mid]<rotateArray[high]:
                high=mid-1
                mid = (low + high) / 2   """      

