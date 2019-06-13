# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:49:08 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        递归式:左子树 插到 右边，右子树 插到末尾。
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root or (root.left is None and root.right is None):
            return
        else:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left is None:
                return
            else:
                temp = root.right
                root.right = root.left
                root.left = None
                p = root.right
                while p.right != None:
                    p = p.right
                p.right = temp
                return
            
'''
执行用时 :
2 ms
, 在所有Java提交中击败了
95.26%
的用户
内存消耗 :
34.8 MB
, 在所有Java提交中击败了
90.65%
的用户

'''