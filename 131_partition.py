# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:09:43 2019

@author: fed
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        split_result = []
        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return 
            for end in range(start+1, len(s)+1):
                split_s = s[start:end]
                if split_s == s[start:end][::-1]:
                    back(end, res+[split_s])

        back()
        return split_result



