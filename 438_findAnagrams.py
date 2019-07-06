# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:10:49 2019

@author: fed
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = len(s)
        n = len(p)
        if m < n:
            return []
        
        s1 = [0] * 26
        s2 = [0] * 26
        for i in range(n):
            s2[ord(p[i]) - 97] += 1
        for i in range(n-1):
            s1[ord(s[i]) - 97] += 1
            
        result = []
        for i in range(m - n + 1):
            s1[ord(s[i+n-1])- 97] += 1
            if s1 == s2:
                result.append(i)
            s1[ord(s[i])- 97] -= 1
        return result        
    
    