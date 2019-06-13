# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:59:51 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        '''
        if not root: 
            return False
        t = sum - root.val
        if not root.left and not root.right:
            return t == 0
        return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)
        '''
        
        if not root:
                return False
        self.res = False
        self.traverse(root, sum)
        return self.res

    def traverse(self, node, cur):
        if not node:
            return
        res = cur - node.val
        if res == 0 and not node.left and not node.right:
            self.res = True

        self.traverse(node.left, res)
        self.traverse(node.right, res)
        
        
