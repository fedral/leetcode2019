# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:00:44 2019

@author: fed
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        self.res = amount + 1
              
        def dfs(c, remain, count):
            if not remain:
                self.res = min(self.res, count)
            
            for i in range(c,len(coins)):
                if  coins[i] <= remain < (self.res - count)*coins[i]:
                    dfs(i, remain-coins[i], count+1)
            
        for i in range(len(coins)):
            dfs(i, amount, 0)
            
        return self.res if self.res <= amount else -1
    
    
    