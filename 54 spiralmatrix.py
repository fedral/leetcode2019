# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:44:14 2019

@author: fed
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix : return []
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            next_matrix = []
            for x in zip(*matrix):
                next_matrix.append(x)
            matrix = next_matrix[::-1]
        return res
    
    
'''
执行用时 : 36 ms, 在Spiral Matrix的Python提交中击败了24.68% 的用户
内存消耗 : 11.8 MB, 在Spiral Matrix的Python提交中击败了13.77% 的用户

'''