#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:54:26 2021

@author: hienpham
"""

class Solution:
    def checkDuplicate(self, arr):
        d = {}
        for i in range(len(arr)):
            if arr[i] != ".":
                val = int(arr[i])
                if val not in d:
                    d[val] = 1
                else:
                    return False
        return True
        
            
    def isValidSudoku(self, board) -> bool:
        #check row
        for line in board:
            if not self.checkDuplicate(line):
                return False
        
        #check col
        for i in range(9):
            valid = {}
            for j in range(9):
                if board[j][i] != ".":
                    val = int(board[j][i])
                    if val in valid:
                        return False
                    else:
                        valid[val] = 1
        #check box
        for i in range(9):
            r = i//3
            c = i%3
            
            arr = board[3*r][3*c:3*(c+1)] + \
                  board[3*r + 1][3*c:3*(c+1)] + \
                  board[3*r + 2][3*c:3*(c+1)]
            
            if not self.checkDuplicate(arr):
                return False
        
        return True
    
    
    def isValidSudoku_v2(self, board) -> bool:
        def isSubBox(i,j,x,y):
            if (i//3 == x//3) and (j//3 == y//3):
                return True
            return False
            
        hashtable = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num not in hashtable.keys():
                        hashtable[num] = [(i,j)]
                    else:
                        for (x,y) in hashtable[num]:
                            if x == i or y == j or isSubBox(i,j,x,y):
                                return False
                        hashtable[num] += [(i,j)]
        return True
    
board =[[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]


ans = Solution().isValidSudoku_v2(board)
                
            
            