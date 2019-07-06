# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:39:51 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def maxDepth(node):
            if not node:
                return 0
            L = maxDepth(node.left)
            R = maxDepth(node.right)
            self.res = max(self.res, L + R)
            return max(L, R) + 1
        
        maxDepth(root)
        return self.res
        
        
        
    