# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:06:07 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        temp = []
        stack = []
        last = nextLast = root
        
        stack.append(root)
        while stack:
            node = stack.pop(0)
            temp.append(node.val)
            if node.left:
                stack.append(node.left)
                nextLast = node.left
            if node.right:
                stack.append(node.right)
                nextLast = node.right
            if node == last:
                res.append(temp[-1])
                temp = []
                last = nextLast
        return res
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    