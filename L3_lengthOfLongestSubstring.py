class Solution:
    #def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):       #滑动窗口的方法，可定义两个指针
        max = 0
        count = 0
        if not s: return max
        ls = list(s)
        space = []
        i = 0
        while i < len(ls):
            if ls[i] in space:
                if count > max: max = count
                ind = ls.index(ls[i])
                ls = ls[ind+1:]
                i = 0
                count = 0
                space = []
            else:
                space.append(ls[i])
                count += 1
                i += 1
                if count > max: max = count
        return max


    # def lengthOfLongestSubstring(self, s):     #暴力解法
    #     max = 0
    #     count = 0
    #     if not s: return max
    #     ls = list(s)
    #     space = []
    #     i = 0
    #     for j in range(len(ls)):
    #         for i in ls[j:]:
    #             if i in space:
    #                 if count > max: max = count
    #                 space = []
    #                 count = 0
    #                 break
    #             else:
    #                 if count > max: max = count
    #                 count += 1
    #                 space.append(i)
    #     return max