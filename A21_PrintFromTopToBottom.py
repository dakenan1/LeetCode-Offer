# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        l = [root]                  #两个辅助空间构造先进先出的队列
        r = []
        while l:
            t = l.pop(0)
            r.append(t.val)
            if t.left:
                l.append(t.left)
            if t.right:
                l.append(t.right)
        return r
        