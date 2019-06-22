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
        for i in range(len(gas)):
            curr += gas[i%len(gas)]
            curr -= cost[i%len(gas)]
            sum += gas[i%len(gas)]-cost[i%len(gas)]
            if curr < 0:
                curr = 0
                start = i+1
                
        if curr >= 0 and sum >= 0:
            return start
        return -1
    
    