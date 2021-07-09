#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:31:52 2021

@author: hienpham
"""
class Solution:
    def isValid(self, val, board, x, y):
        # check row
        if str(val) in board[x]:
            return False
        
        # check col
        for i in range(9):
            if board[i][y] == str(val):
                return False
        
        # check subbox
        r, c = x//3, y//3
        
        arr = board[3*r][3*c:3*(c+1)] + \
              board[3*r+1][3*c:3*(c+1)] + \
              board[3*r+2][3*c:3*(c+1)]
        
        if str(val) in arr:
            return False
        
        return True
    
    
    def isComplete(self, board):
        if "." in board[8]:
            return False
        return True
    
    
    def backtrack(self, val, board, idx, pos):
        
        x, y = pos[idx]
        for num in range(val, 10):
            if self.isValid(num, board, x, y):
                board[x][y] = str(num)
                
                if idx + 1 < len(pos):
                    self.backtrack(1, board, idx+1, pos)
                else:
                    return
                
            if self.isComplete(board):
                return
            else:
                board[x][y] = "."
        return
    
    
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # create a hash map of empty positions
        idx = 0
        pos = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    pos[idx] = [i, j]
                    idx += 1
        
        self.backtrack(1, board, 0, pos)
        
        return board
    
    
board =  [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans = Solution().solveSudoku(board)