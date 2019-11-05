import re
class Solution:
    #def myAtoi(self, str: str) -> int:
    def myAtoi(self, str):
        str = str.strip()
        if not str: return 0
        ls = list(str)
        if len(ls) == 1:
            return int(ls[0]) if ls[0].isnumeric() else 0
        if (ls[0] == '+' or ls[0] == '-'):
            if not ls[1].isnumeric(): return 0
            else:
                num = re.findall('\d+', ''.join(ls))
                if ls[0] == '+': return int(num[0]) if int(num[0])<2**31-1 else 2**31-1
                else: return -int(num[0]) if int(num[0])<2**31 else -2**31
        elif ls[0].isnumeric():
            num = re.findall('\d+',''.join(ls))
            return int(num[0]) if int(num[0])<2**31-1 else 2**31-1
        else: return 0
