# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:45:54 2019

@author: fed
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==1):
            return 0
        start,end=0,0
        steps=1
        maxindex=0
        while True:
            for i in range(start,end+1):
                maxindex=max(maxindex,nums[i]+i)
            if(maxindex>=len(nums)-1):
                return steps
            steps+=1
            start=end+1
            end=maxindex
            
        
        