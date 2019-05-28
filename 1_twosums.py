# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:23:18 2019

@author: fed
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # O(n^2) 
        l = len(nums)
        for i in range(l):
            for k in range(i+1,l):
                if nums[k] + nums[i] == target:
                    return [i,k]
        '''      
        执行用时 : 4072 ms, 在Two Sum的Python提交中击败了25.76% 的用户
        内存消耗 : 12.5 MB, 在Two Sum的Python提交中击败了35.27% 的用户
        '''
        
        # O(n)
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
        '''
        执行用时 : 36 ms, 在Two Sum的Python提交中击败了99.85% 的用户
        内存消耗 : 13.1 MB, 在Two Sum的Python提交中击败了11.15% 的用户
        
        '''
        
        