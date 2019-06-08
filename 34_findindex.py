# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:59:49 2019

@author: fed
"""

class Solution(object):
    def searchRange(self, nums, target):

        res = [-1, -1]
        n = len(nums)-1
        if not nums:
            return res
        
        l = 0 
        r = n
        m = 0
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        if nums[m] == target:
            i, j = m, m
            while i > 0 and nums[i-1] == target:
                i -= 1
            while j < n and nums[j+1] == target:
                j += 1
            res = [i, j]
        return res
    
'''

执行用时 : 88 ms, 在Find First and Last Position of Element in Sorted Array的Python提交中击败了98.59% 的用户
内存消耗 : 13 MB, 在Find First and Last Position of Element in Sorted Array的Python提交中击败了33.26% 的用户

'''
