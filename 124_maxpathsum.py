# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:08:04 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def sum(root):
            if not root:
                return 0
            l = sum(root.left)
            r = sum(root.right)
            # 记录最大值
            nonlocal ret
            ret = max(ret , l+r+root.val , root.val , root.val+l , root.val+r)
            # 返回
            return max(root.val , root.val+l , root.val+r)
        
        ret = float('-inf')
        sum(root)
        return ret        
    
    
'''

执行用时 :
124 ms
, 在所有Python3提交中击败了
96.88%
的用户
内存消耗 :
20.8 MB
, 在所有Python3提交中击败了
67.00%
的用户

'''