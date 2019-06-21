# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:35:13 2019

@author: fed
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        for interval in intervals:
            if interval[0]<=newInterval[0] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            if interval[0]<=newInterval[1] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        res = []
        for interval in intervals:
            if not (interval[0]>=newInterval[0] and interval[1] <=newInterval[1]):
                res.append(interval)

        res.append(newInterval)
        for i in range(len(res)-1, 0, -1):
            if res[i-1][0] > res[i][0]:
                res[i-1], res[i] = res[i], res[i-1]
        return res

    
    
    
    
    