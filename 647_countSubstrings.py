# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:12:11 2019

@author: fed
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        i = j = res = 0
        while i < n:
            while j < n and s[i] == s[j]:
                j += 1
            res += (1 + j - i) * (j - i) // 2
            
            l, r = i - 1, j
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            i = j
        return res
    
    
    