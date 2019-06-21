# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:52:04 2019

@author: fed
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        while(l<len(nums)-2):
            r=l+2
            if nums[r]==nums[l]:
                del nums[r]
            else:
                if nums[r]!=nums[r-1]:
                    l=r
                else:
                    l=l+1
        return len(nums)
    
    
    
    
    
    
    