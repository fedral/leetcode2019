# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:50:09 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        self.dfs(root, ret, 0)
        return sum(ret)

    def dfs(self, root, ret, num):
        if not root:
            return
        if not root.left and not root.right:
            ret.append(num * 10 + root.val)
            return
        self.dfs(root.left, ret, num * 10 + root.val)
        self.dfs(root.right, ret, num * 10 + root.val)
        
        
'''
执行用时 :24 ms, 在所有Python提交中击败了89.73%的用户
内存消耗 :12.1 MB, 在所有Python提交中击败了8.21%的用户

'''

































