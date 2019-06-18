# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:20:16 2019

@author: fed
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res=nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):  
            l,r=i+1,len(nums)-1
            while l<r:
                ss=nums[i]+nums[l]+nums[r]
                if abs(ss-target) < abs(res-target):
                    res = ss
                if ss>target:
                    r-=1
                elif ss<target:
                    l+=1
                else:
                    return res
        return res
    
    
    