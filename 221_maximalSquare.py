# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:04:08 2019

@author: fed
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        length = 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    length = max(length, dp[i][j])
        return length*length





