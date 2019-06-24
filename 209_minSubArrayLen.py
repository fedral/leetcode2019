# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:35:54 2019

@author: fed
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, a, r = 0, 0, float('inf')
        for j in range(len(nums)):
            a += nums[j]
            while a >= s:
                r = min(r, j - i + 1)
                a -= nums[i]
                i += 1
        return 0 if r == float('inf') else r
    
    
    