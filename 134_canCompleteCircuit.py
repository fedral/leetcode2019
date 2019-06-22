# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:21:36 2019

@author: fed
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curr = 0
        start = 0
        sum = 0
        for i in range( len(gas) ): 
            curr += gas[i]-cost[i]
            sum  += gas[i]-cost[i]
            
            if curr < 0:
                curr = 0
                start = i+1

        return start  if sum >= 0 else -1
    
    