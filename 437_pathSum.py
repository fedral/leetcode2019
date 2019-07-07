# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:14:18 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def dfs(root,sum):
            count=0  #记录路径个数
            if not root:
                return 0
            if root.val==sum:
                count+=1
            count+=dfs(root.left,sum-root.val)
            count+=dfs(root.right,sum-root.val)
            return count
        return dfs(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)

        
    def pathsum(root, sum)
        def dfs(root, prevSum, sum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - sum in rec:
                count += rec[currSum - sum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, sum)
            count += dfs(root.right, currSum, sum)
            rec[currSum] -= 1
            return count
            
        rec = {0:1}
        return dfs(root, 0, sum)