# -*- coding:utf-8 -*-
def Quick_array(a,left,right):
    if (left >= right):
        return a
    i = left
    j = right
    key = a[left]   #一轮始终只需要比较一个
    while(i<j):
        while (i<j and key<=a[j]):
            j -= 1
        a[i] = a[j]
        while (i<j and key>=a[i]):
            i += 1
        a[j] = a[i]
    a[i] = key
    print(a)
    Quick_array(a,left,i-1)
    print('left is finish')
    Quick_array(a,i+1,right)
    print('right is finish')


             
        

"""     for k in range(len(array)-2):
        flag = j
        if array[i] > array[flag]:
            array[i],array[j-k] = array[j-k],array[i] """

