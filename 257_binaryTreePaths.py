# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:20:05 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if not root:
            return []
        res = []
        
        def scan(root, tmp):
            # tmp.append(str(root.val))
            if root.left is None and root.right is None:
                tmp.append(str(root.val))
                res.append("->".join(tmp))
            
            if root.left:
                scan(root.left, tmp+[str(root.val)])
            if root.right:
                scan(root.right, tmp+[str(root.val)])
        
        scan(root, [])
        return res



