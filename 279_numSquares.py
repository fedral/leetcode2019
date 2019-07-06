# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:45:24 2019

@author: fed
"""



class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n+1):
            dp.append(min( dp[-j*j] for j in range(1, 1 + int(i**0.5)) ) + 1)
        return dp[-1]













