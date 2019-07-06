# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:34:16 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        
        def dfs(root):
            if not root: 
                return root
            dfs(root.right)
            self.sum = self.sum + root.val
            root.val = self.sum
            dfs(root.left)
            return root
        
        return dfs(root)
    
    