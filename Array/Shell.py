# -*- coding: utf-8 -*-
def shell(arr):         #一般的初次取序列的一半为增量，以后每次减半，直到增量为1。
    n=len(arr) 
    h=1 
    while h<n/3:  
        h=3*h+1 
        while h>=1:  
            for i in range(h,n):   
                j=i   
                while j>=h and arr[j]<arr[j-h]:    
                    arr[j], arr[j-h] = arr[j-h], arr[j]    
                    j-=h  
            h=h//3 
    print arr