class Solution:
    #def strStr(self, haystack: str, needle: str) -> int:
    def strStr(self, haystack, needle):          # sunday
        if not needle: return 0
        if not haystack: return -1
        hay = list(haystack)
        nee = list(needle)
        dict = {}
        ln = len(nee)
        lh = len(haystack)
        if lh <= ln : return 0 if nee == hay else -1
        for i in range(ln):
            dict[nee[i]] = i
        j = 0       
        while j < lh - ln:
            if nee == hay[j:j+ln]:
                return j
            else:               
                if hay[j+ln] in dict:        # 窗口后一个不是j+ln+1
                    j += ln - dict.get(hay[j+ln])
                else : j += ln 
        
        return -1 if nee != hay[j:lh] else j     #判断最后一个，放在while循环里执行会超界限