# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:49:49 2019

@author: fed
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows == 1:
            return s
        s_Rows = [""] * numRows
        i  = 0
        n = len(s)
        while i < n:
            for j in range(numRows):
                if i < n:
                    s_Rows[j] += s[i]
                    i += 1
            for j in range(numRows-2,0,-1):
                if i < n:
                    s_Rows[j] += s[i]
                    i += 1
        return "".join(s_Rows)
    

'''
执行用时 : 40 ms, 在ZigZag Conversion的Python提交中击败了98.28% 的用户
内存消耗 : 11.8 MB, 在ZigZag Conversion的Python提交中击败了26.08% 的用户

'''