# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:54:03 2019

@author: fed
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0]*n for _ in range(n)]
        x, y, dx, dy = 0, 0, 0, 1
        for i in range(1, n**2+1):
            result[x][y] = i
            if result[(x+dx)%n][(y+dy)%n]:  # 这里理解判断条件是关键
                dx, dy = dy, -dx
            x += dx
            y += dy
        return result
    
'''
执行用时 : 28 ms, 在Spiral Matrix II的Python提交中击败了78.26% 的用户
内存消耗 : 11.6 MB, 在Spiral Matrix II的Python提交中击败了36.14% 的用户

'''

# python3
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r, n = [[n**2]], n**2
        while n > 1: 
            n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
        return r


