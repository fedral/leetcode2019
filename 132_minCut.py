# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:13:47 2019

@author: fed
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == s[::-1]:
            return 0
        
        for i in range(1, len(s)):
            if s[:i]==s[i-1::-1] and s[i:]==s[:i-1:-1]:
                return 1
            
        dp=[i for i in range(-1, len(s))]
        for i in range(len(s)):
            t=0
            while i-t>=0 and i+t<len(s) and s[i-t]==s[i+t]:
                dp[i+t+1]=min(dp[i+t+1],dp[i-t]+1)
                t+=1
            t=0
            while i-t>=0 and i+t+1<len(s) and s[i-t]==s[i+t+1]:
                dp[i+t+2]=min(dp[i+t+2],dp[i-t]+1)
                t+=1
        return dp[-1]
    
    