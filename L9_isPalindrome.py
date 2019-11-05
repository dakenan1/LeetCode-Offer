class Solution:
    #def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):            #完全不适用字符串，考虑数据溢出，半翻转
        if x < 0: return False
        elif x == 0: return True
        elif x % 10 == 0:return False        #处理不了50.60等末尾为0的数
        y = 0
        while x > 0:
            tmp = x % 10
            y = y*10 + tmp
            x = x // 10
            if x == y: return True               #处理奇偶位回文
            elif x == y//10: return True
            elif x < y: return False
        return False
