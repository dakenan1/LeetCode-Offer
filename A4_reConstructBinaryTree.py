# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        #T = TreeNode()
        if not TreeNode:
            return None
        else:
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1+tin.index(pre[0])], tin[:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[1+tin.index(pre[0]):], tin[1+tin.index(pre[0]):])
            # 类内调用务必加上self
            return root