# -*- coding:utf-8 -*-
def Quick_array2(array):
    if len(array) >= 2:   #空集以及完全分开之后
        l = []
        r = []
        key = array[0]
        array.pop(0)
        for i in range(len(array)):
            if array[i] <= key:   #顺序排列
                l.append(array[i])
            else:
                r.append(array[i])
        return Quick_array2(l) + [key] + Quick_array2(r)
    else:
        return array

    