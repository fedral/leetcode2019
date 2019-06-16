# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:00:49 2019

@author: fed
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:   #优化点：直接从局部最小开始 
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max( longest_streak, current_streak )

        return longest_streak


