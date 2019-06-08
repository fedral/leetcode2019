# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:15:34 2019

@author: fed
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i-stack[-1] - 1)
            stack.append(i)
        return res
    
    
    
    
'''
执行用时 : 44 ms, 在Trapping Rain Water的Python提交中击败了96.91% 的用户
内存消耗 : 12.2 MB, 在Trapping Rain Water的Python提交中击败了35.90% 的用户
'''

