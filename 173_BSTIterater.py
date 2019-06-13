# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:12:56 2019

@author: fed
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        temp = self.stack.pop()
        res = temp.val
        temp = temp.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return res        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



'''
执行用时 :
84 ms
, 在所有Python提交中击败了
92.98%
的用户
内存消耗 :
21.3 MB
, 在所有Python提交中击败了
27.71%
的用户
'''