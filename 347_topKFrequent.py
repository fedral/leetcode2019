# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:01:46 2019

@author: fed
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
            
        from collections import defaultdict
        lookup = defaultdict(int)
        for num in nums:
            lookup[num]+=1
        sorted_x = sorted(lookup.items(),key=lambda x: x[1], reverse=True)       
        return [x[0] for x in sorted_x[0:k]]
        
    
    