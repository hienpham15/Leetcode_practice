#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:19:31 2021

@author: hienpham
"""
class Solution:
    def trans_mat(self, mat):
        n = len(mat[0])
        return [[mat[i][n-1 - j] for i in range(len(mat))] for j in range(n)]
    
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        first_row = matrix.pop(0)
        ans = []
        while first_row:
            print(first_row)
            ans += first_row
            if not matrix:
                return ans
            else:
                matrix = self.trans_mat(matrix)
            first_row = matrix.pop(0)
            
        return ans