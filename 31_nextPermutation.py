# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:56:01 2019

@author: fed
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # step1 find first decrese
        i=len(nums)-2
        while i>=0 and nums[i+1]<=nums[i] :
            i-=1
        # step2 find ele for swap
        if i>=0:
            j=len(nums)-1
            while j>=0 and nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        
        # step3 permute to next
        p1,p2=i+1,len(nums)-1
        while p1<p2:
            nums[p1],nums[p2] = nums[p2],nums[p1]
            p1+=1
            p2-=1  
            
'''
执行用时 : 32 ms, 在Next Permutation的Python提交中击败了98.50% 的用户
内存消耗 : 11.7 MB, 在Next Permutation的Python提交中击败了41.18% 的用户
'''      
            





















