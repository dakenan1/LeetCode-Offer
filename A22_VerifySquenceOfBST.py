# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence.pop(-1)
        if sequence[0] < root:
            while sequence and sequence[0] < root:
                sequence.pop(0)
            if not sequence:
                return True
        while sequence and sequence[0] > root:
            sequence.pop(0)
        if not sequence: return True
        else: return False
            



        
        