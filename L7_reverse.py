class Solution:
    #def reverse(self, x: int) -> int:
    def reverse(self, x):
        flag = 0
        y = 0
        if x < 0: 
            x = -x
            flag = 1
        if x % 10 == 0: x = x//10
        while x > 0:
            pop = x % 10
            x = x // 10  
            if y > (2**31)//10 or ( y == (2**31)//10 and pop > 7):  return 0
            else:   y = y*10 + pop
        if flag == 1:
            y = -y
        return y