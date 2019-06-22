# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:36:24 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        is_first = True
        pre, p1, p2 = None, None, None

        def in_order(root: TreeNode):
            nonlocal pre, is_first, p1, p2
            if root == None:
                return
            in_order(root.left)
            
            if pre != None and pre.val >= root.val:
                if is_first:
                    p1 = pre
                    p2=root
                    is_first = False
                else:
                    p2 = root
            pre = root
            in_order(root.right)
            
        in_order(root)
        p1.val, p2.val = p2.val, p1.val
        
        