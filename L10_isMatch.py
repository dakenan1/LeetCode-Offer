class Solution:
    #def isMatch(self, s: str, p: str) -> bool:
    def isMatch(self, s, p):  
        ss = list(s)
        pp = list(p)
        j = 0
        i = 0
        flag = False
        while i < len(pp):           
            if pp[i] == ss[j]:
                j += 1
                i += 1
            elif pp[i] == '.':
                j += 1
                i += 1
            elif pp[i] == '*':
                if pp[i-1] == '.': return True
                elif pp[i-1] == '*': continue
            
            else:

            if j == len(ss): return True
