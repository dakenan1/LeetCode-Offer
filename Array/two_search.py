# -*- coding:utf-8 -*-
def two_search(array, key):       #直接改变首尾位置而不是改变搜索的list
    low = 0                         # 最小数下标    
    high = len(array) - 1       # 最大数下标    
    while low <= high:        
        mid = (low + high) // 2     # 中间数下标        
        if array[mid] == key:   # 如果中间数下标等于key, 返回            
            return mid        
        elif array[mid] > key:  # 如果key在中间数左边, 移动high下标            
            high = mid - 1        
        else:                       # 如果key在中间数右边, 移动low下标            
            low = mid + 1    
    return # key不存在, 返回None


"""     if len(array) < 1:         # too many if!!! 
        return
    else:
        mid = len(array)/2  
        if mid == 0:
            if array[mid] == key:
                return mid
            else:
                return
        else:
            if array[mid] == key:
                return mid
            elif array[mid] > key:
                two_search(array[:mid-1],key)
            elif array[mid] < key:
                two_search(array[mid:],key) """
        
        

    