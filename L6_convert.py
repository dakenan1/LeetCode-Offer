class Solution:
    #def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):                  # 题目描述成Z字型就是在提示要按行分类                                                
        re = []                                     # 单纯找跳过的规律不容易
        ls = list(s)
        if numRows == 1:   return s
        for i in range(numRows):
            re.append([])
        step = 0
        flag = 1
        while ls:            
            re[step].append(ls.pop(0))
            step += flag
            if step == 0 or step == numRows -1:
                flag = -flag                         # flag控制转向
        r = []
        for j in range(numRows):
            r += re[j]
        return ''.join(r)

            

            