#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:41:17 2021

@author: hienpham
"""
class Solution:
    def backtrack(self, i, j, board, word):
        m = len(board)
        n = len(board[0])
        
        a = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        if not word:
            return True
        
        if i < 0 or i > m - 1:
            return False
        if j < 0 or j > n - 1:
            return False
        
        
        
        ans = False
        if board[i][j] == word[0]:
            tmp = board[i][j]
            board[i][j] = "*"
            for d in a:
                ans = ans or self.backtrack(i + d[0], j + d[1], board, word[1:])
            board[i][j] = tmp
            
        return ans
        
            
        
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        head_list = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    head_list.append((i, j))
        
        for i in range(len(head_list)):
            x, y = head_list[i]
            ans = self.backtrack(x, y, board, word)
            if ans:
                return True
            
        return False
    
board = [["a"]]
word = "a"
ans = Solution().exist(board, word)