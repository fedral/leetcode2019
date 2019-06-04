# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 10:56:47 2019

@author: fed
"""


class Solution:
    
    def solveNQueens(self, n):
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output
    
'''
执行用时 : 52 ms, 在N-Queens的Python提交中击败了95.50% 的用户
内存消耗 : 12.1 MB, 在N-Queens的Python提交中击败了26.36% 的用户
'''           




class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        s = "."*n
        def bt(i,tmp,col,diag1,diag2):
            if(i==n):
                res.append(tmp)
            for j in range(n):
                if( not j in col and not i+j in diag1 and not i-j in diag2 ):
                    bt( i+1,tmp+[s[:j]+"Q"+s[j+1:]], col+[j], diag1+[i+j],    )
        bt(0,[],[],[],[])
        return res

 '''
 执行用时 : 52 ms, 在N-Queens的Python提交中击败了95.54% 的用户
内存消耗 : 11.7 MB, 在N-Queens的Python提交中击败了40.91% 的用户
 '''






