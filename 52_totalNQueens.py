# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:25:13 2019

@author: fed
"""



class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        
        def backtrack(i,col,z_diagonal,f_diagonal):
            if i == n:return  True
            for j in range(n):
                if j not in col and i + j not in  z_diagonal and i - j not in f_diagonal:
                    if backtrack(i+1, col | {j}, z_diagonal |{i + j} , f_diagonal |{i - j}  ) :
                        self.res += 1
            return False
        backtrack(0,set(),set(),set())    
        return self.res




      # bitmap
      self.count = 0
        def dfs(row=0, col=0, pie=0, na=0):
            if row == n:
                self.count += 1
                return
            
            bits = ~(col | pie | na) & ((1 << n) - 1)
            while bits != 0:
                pos = bits & -bits
                dfs(row + 1, col | pos, (pie | pos) << 1, (na | pos) >> 1)
                bits &= bits - 1

        dfs()
        return self.count