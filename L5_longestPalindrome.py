class Solution:
    #def longestPalindrome(self, s: str) -> str:      #暴力解法，O(n^2)
    def longestPalindrome(self, s):
        if not s : return ''
        st = list(s)
        re = []
        max = 0
        for i in range(len(st)):
            for j in range(1,1+len(st)-i):
                if j%2 == 0:
                    l_st = st[i:i+j]
                    re_st = st[i+j//2:i+j]
                    re_st.reverse()
                    if self.cmp1(re_st,st[i:i+j//2]) and j > max:
                        max = j
                        re.append(''.join(st[i:i+j]))
                else:
                    l_st = st[i:i+j]
                    re_st = st[i+j//2:i+j]
                    re_st.reverse()
                    if self.cmp1(re_st,st[i:1+i+j//2]) and j > max:
                        max = j
                        re.append(''.join(st[i:i+j]))
        return re[-1]
    def cmp1(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
                
