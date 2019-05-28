# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:15:08 2019

@author: fed
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        if len(nums) <= 1:
            return [nums]
        out = []
        perms = self.permuteUnique(nums[1:])
        for perm in perms:
            for i in range(0, len(perm)+1):
                p = perm[:i] + [nums[0]] + perm[i:]
                if p not in out:
                    out.append(p)
        return out
        '''
        执行用时 : 96 ms, 在Permutations II的Python提交中击败了43.15% 的用户
        内存消耗 : 12 MB, 在Permutations II的Python提交中击败了33.68% 的用户
        '''
        
        
        