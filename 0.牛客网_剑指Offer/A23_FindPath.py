# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:               #未完成                 
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if not root.left and not root.right and root.val == expectNumber:            #递归，这里会返回之前的路径，因此不能直接返回root.val == expectNumber的结果
            return [root.val] 
        path = []
        sum = root.val
        while sum < expectNumber:

