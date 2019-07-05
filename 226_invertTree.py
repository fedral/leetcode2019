# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:12:03 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if not root.left  and not root.right:
            return root
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
        
    
    
    