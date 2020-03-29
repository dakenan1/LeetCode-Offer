# -*- coding:utf-8 -*-            #三次判断返回0的情况
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:             #空集
            return 0
        flag = 0
        string = map(str,s)
        if string[0] == '+':
            string.pop(0)
        elif string[0] == '-':
            string.pop(0)
            flag = 1
        i = 0
        while string:
            if string[0] == '0':
                string.pop(0)
                continue
            else:
                for i in string:                  #含有非数字字符
                    if ord(i) > 57 or ord(i) < 48:
                        return 0
                break
        if not string:                      #仅含有0的情况
            return 0
        num = ''.join(string)
        num = int(num)
        if flag == 1:
            return (~num)+1
        else:
            return num
        