class Solution(object):
    #def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits):
        lookup = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not digits:
            return []
        res = [""]
        for num in digits:              # 牛逼的三循环！！
            next_res = []
            for alp in lookup[num]:
                for tmp in res:
                    next_res.append(tmp + alp)            
            res = next_res              # 更新
        return res

    # def __init__(self):
    #     self.m = {
    #         '2':'abc', '3':'def', '4':'ghi',
    #         '5':'jkl', '6':'mno', '7':'pqrs',
    #         '8':'tuv', '9':'wxyz'
    #     }
    # def letterCombinations(self, digits):
    #     if not digits: return ''
    #     dg = list(digits)
    #     for i in range(len(dg)):

            
