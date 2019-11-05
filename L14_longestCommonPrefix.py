class Solution:
    #def longestCommonPrefix(self, strs: List[str]) -> str:     
    def longestCommonPrefix(self, strs):   
        s = ""
        for i in zip(*strs):                # 提取相同位置的元素
            if len(set(i))==1:              # 判断所有元素是否等于同一个
                s += i[0]
            else:
                break           
        return s 


#    #按照字典序，因此第一个跟最后一个必前缀相同证明其他的都相同
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs: return ''
#         elif len(strs)== 1: return strs[0]
#         strs.sort()
#         s1 = list(strs[0])
#         s2 = list(strs[-1])
#         re = []
#         for i in range(len(s1)):
#             if s1[i] == s2[i]:
#                 re.append(s1[i])
#             else: break
#         return ''.join(re)
