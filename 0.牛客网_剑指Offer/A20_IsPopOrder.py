# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l = []
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV:
            return False
        while pushV:
            if popV[0] == pushV[0]:
                popV.pop(0)
                pushV.pop(0)   
            else:
                self.l.append(pushV.pop(0))
        self.l.reverse()    
        return self.l == popV               # return 函数不能太复杂


"""         if not pushV:                   #！！！千万别滥用递归！！！
            flag = self.l.reverse() == popV
            return flag 
        else:   
            while popV[0] != pushV[0]:
                self.l.append(pushV.pop(0))
            popV.pop(0)
            pushV.pop(0)
        re = self.IsPopOrder(pushV, popV)
        return re """