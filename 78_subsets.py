# -*- coding: utf-8 -*-
"""
Created on Wed May 29 06:30:08 2019

@author: fed
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: 
            return [[]]
        res=[] 
        for p in self.subsets(nums[1:]):
            res.append(p)
            res.append(nums[:1]+p) 
        return res   
'''
执行用时 : 32 ms, 在Subsets的Python提交中击败了88.42% 的用户
内存消耗 : 12 MB, 在Subsets的Python提交中击败了16.99% 的用户
'''




