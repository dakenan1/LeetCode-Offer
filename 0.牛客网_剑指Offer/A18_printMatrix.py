# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        else:
            l = []
            while matrix:
                l = l + matrix.pop(0)
                if not matrix:
                    break
                matrix = self.turn(matrix)
            return l
    def turn(self,matrix):
        high = len(matrix)
        weigh = len(matrix[0])
        B = []
        for j in range(weigh):
            A = []
            for i in range(high):
                A.append(matrix[i][j])
            print 'A===',A    
            B.append(A)      
        B.reverse()
        print 'B====',B
        return B
            


















"""         result=[]
        while matrix:
            result=result+matrix.pop(0)
            if not matrix:
                break
            matrix=self.turn(matrix)
        return result
    def turn(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        B=[]
        for i in range(c):
            A=[]
            for j in range(r):
                A.append(matrix[j][i])
            print 'A===',A
            B.append(A)
            print 'B===',B
        B.reverse()
        print 'Br===',B
        return B """
