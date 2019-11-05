class Solution:
    #def isValid(self, s: str) -> bool:
    def isValid(self, s):   
        if not s: return True
        send = list(s)
        rec = []
        sample = {'(':')', '[':']', '{':'}'}
        while send:
            tmp = send.pop(0)
            if rec and tmp in sample.values():
                val = list(filter(lambda x:tmp == x[1],sample.items()))
                if val[0][0] == rec[-1]: 
                    rec.pop()
                else: return False
            elif tmp in sample.keys(): rec.append(tmp)
            else: return False
        if rec: return False
        return True

# class Solution:
#     def isValid(self, s: str) -> bool:
#         dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
#         stack = ['?']
#         for c in s:
#             if c in dic: stack.append(c)
#             elif dic[stack.pop()] != c: return False  # 若不是三种开括号则必然是闭括号，
#         return len(stack) == 1                        # 反向从stack中推出key看是否是对应的value
#                                                       # 另外的，可以加入长度为奇数提前跳出等优化

