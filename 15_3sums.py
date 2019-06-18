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
        
        
        '''
        # O(n^3)
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
    
    
        
        '''
        # O(n)
        执行用时 : 528 ms, 在3Sum的Python提交中击败了91.99% 的用户
        内存消耗 : 15 MB, 在3Sum的Python提交中击败了48.61% 的用户
        '''
        
        
        result = list()
        nums_len = len(nums)
        if nums_len < 3:
            return result
        l, r, dif = 0, 0, 0
        nums.sort()
        
        for i in range(nums_len - 2):
            if nums[i] > 0: break  #去除多余运算
            if i > 0 and nums[i - 1] == nums[i]: continue  #去重

            l = i + 1
            r = nums_len - 1
            dif = -nums[i]
            while l < r:
                if nums[l] + nums[r] == dif:
                    result.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l + 1]: l += 1 #去重
                    while l < r and nums[r] == nums[r - 1]: r -= 1 #去重
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < dif:
                    l += 1
                else:
                    r -= 1
        
        return result


