# -*- coding:utf-8 -*-
def Bubble_array(array):   #array >> list
    if not array:
        return
    for j in range(len(array)-1):
        change = 0
        for i in range(len(array)-j-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]  #python 不需要中间变量
                #a = array[i]
                #array[i] = array[i+1]
                #array[i+1] = a  
                change +=1
        if change == 0:
            return array  
