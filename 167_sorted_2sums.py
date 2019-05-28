# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:06:19 2019

@author: fed
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''
        有序数组>>对撞指针 [空间O(1),时间O(n)]  优于hash table [空间O(n),时间O(n)] 
        执行用时 : 64 ms, 在Two Sum II - Input array is sorted的Python提交中击败了94.29% 的用户
        内存消耗 : 12 MB, 在Two Sum II - Input array is sorted的Python提交中击败了23.22% 的用户
        
        '''
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []
    
    
    