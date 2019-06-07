# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:58:39 2019

@author: fed
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
      
        if len(nums) <= 1:
            return [nums]
        out = []
        perms = self.permute(nums[1:])
        for perm in perms:
            for i in range(0, len(perm)+1):
                p = perm[:i] + [nums[0]] + perm[i:]
                out.append(p)
        return out
    
'''
执行用时 : 28 ms, 在Permutations的Python提交中击败了98.57% 的用户
内存消耗 : 11.9 MB, 在Permutations的Python提交中击败了17.96% 的用户
'''
    
    

# backtrack
def backtrack(first = 0):
    if first == n:  
        output.append(nums[:])
    for i in range(first, n):
        nums[first], nums[i] = nums[i], nums[first]
        backtrack(first + 1)
        nums[first], nums[i] = nums[i], nums[first]
nums=[1,2,3,4]
n = len(nums)
output = []
backtrack()



    
    
    