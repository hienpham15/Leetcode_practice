#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:29:26 2021

@author: hienpham
"""
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        return [[matrix[n-1 - i][j] for i in range(n)] for j in range(len(matrix[0]))]
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        val = n**2
        
        spiral = [[val]]
        while val > 1:
            first_row = []
            spiral = self.rotate(spiral)
            k = len(spiral[0])
            for i in range(k):
                first_row.insert(0, val - 1)
                val -= 1
                
            print(first_row)
            spiral.insert(0, first_row)
            
            print(spiral)
        
        return spiral