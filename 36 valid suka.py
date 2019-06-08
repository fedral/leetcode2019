# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:36:19 2019

@author: fed
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True

'''
执行用时 : 104 ms, 在Valid Sudoku的Python提交中击败了82.81% 的用户
内存消耗 : 11.8 MB, 在Valid Sudoku的Python提交中击败了21.33% 的用户

'''