# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #def __init__(self):
        #self.Depth = None
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        else:
            return 1 + max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))