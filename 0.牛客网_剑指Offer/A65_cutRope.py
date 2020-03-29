# -*- coding:utf-8 -*-        #n<=3时，不剪断为最好，因此考虑往后都尽量转换为2,3
class Solution:
    def __init__(self):
        self.flag = 1
    def cutRope(self, number):
        # 动态规划法
        # # write code here    
        # if number == 2 or number == 3:
        #     return number - self.flag
        # elif number == 1:
        #     return 1
        # else:
        #     self.flag = 0
        #     return max(self.cutRope(number-2)*2,self.cutRope(number-3)*3)

        # 因为最佳的组合能且只能包含2和3，因此只需要将M-1最佳组合修改即可
        max = [[0],[1],[1,1],[1,2]]
        n = 4
        # if number < len(max):
        #     return max[number][0]
        while n <= number:
            max.append(max[n-1])
            if 1 in max[n]:
                max[n].remove(1)
                max[n] += [2]
            elif (2 in max[n]):
                max[n].remove(2)
                max[n] += [3]
            else:
                max[n].remove(3)
                max[n] += [2,2]
            n += 1
        result = 1
        for i in max[number]:
            result *= i
        return result

        