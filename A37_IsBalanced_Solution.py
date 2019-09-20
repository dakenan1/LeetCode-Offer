# -*- coding:utf-8 -*- 
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:                         #后续遍历？
    def __init__(self):
        self.maxD = 0
        self.minD = 0
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        else:
            self.maxD = 1 + max(self.IsBalanced_Solution(pRoot.left),self.IsBalanced_Solution(pRoot.right))
            self.minD = 1 + min(self.IsBalanced_Solution(pRoot.left),self.IsBalanced_Solution(pRoot.right))
        return abs(self.maxD - self.minD) <= 1        