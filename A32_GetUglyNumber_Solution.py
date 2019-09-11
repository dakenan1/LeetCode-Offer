# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):        
        # write code here
        if index <= 0:
            return ''
        if index == 1:
            return 1        
        x, y, z = 2, 3, 5
        index2, index3, index5 = 1, 1, 1
        re = [0,1]
        while True:    
            if x == min(x,y,z):
                if x > re[-1]:
                    re.append(x)
                index2 += 1
                x = re[index2] * 2
            elif y == min(x,y,z):
                if y > re[-1]:
                    re.append(y)
                index3 += 1
                y = re[index3] * 3
            elif z == min(x,y,z):
                if z > re[-1]:
                    re.append(z)
                index5 += 1
                z = re[index5] * 5
            if len(re) == index+1:
                break
        return re[index]


"""     ugly = [0,1]                #判断，超时！！！        
        if index <= 0:
            return ''
        if index == 1:
            return ugly[1]
        n = 1
        times = 1
        flag = 0
        while times != index:
            if flag == 0:
                mid = n
            if mid == 2 or mid==3 or mid==5:
                ugly.append(n)
                times += 1
                n += 1
                flag = 0
                continue

            if mid%2 == 0: 
                flag = 1
                mid = mid/2 
                continue
            elif mid%3 == 0:
                flag = 1
                mid = mid/3
                continue 
            elif mid%5 == 0:
                flag = 1
                mid = mid/5
                continue
            else:
                n += 1
                flag = 0
        return ugly[index]
 """