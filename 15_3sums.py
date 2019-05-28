# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:56:41 2019

@author: fed
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # O(n^3)
        '''
        超出时间限制
        '''
        res=[]
        l=len(nums)
        for i in range(0, l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):                
                    if nums[i]+nums[j]+nums[k] == 0:
                        triple = sorted([nums[i],nums[j],nums[k]])
                        if triple not in res:
                            res.append(triple)
        return res

