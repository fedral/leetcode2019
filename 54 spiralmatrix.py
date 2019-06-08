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

def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

'''

执行用时 : 16 ms, 在Spiral Matrix的Python提交中击败了98.47% 的用户
内存消耗 : 11.5 MB, 在Spiral Matrix的Python提交中击败了37.92% 的用户
'''
