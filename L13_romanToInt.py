class Solution:
    #def romanToInt(self, s: str) -> int:
    def romanToInt(self, s):
        roma = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #roma = sorted(roma.items(),key = lambda x:-x[1])                #x:加负号为逆序,但变成了列表
        ss = list(s)
        re = []
        for num in ss:
            if num in roma.keys():
                re.append(int(roma[num]))
            else: return 0
        sum_num = 0
        for j in range(len(re)-1):
            if re[j] < re[j+1]: re[j] = -re[j]       
        sum_num = sum(re)
        return sum_num
