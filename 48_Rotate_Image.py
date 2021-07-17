#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:27:45 2021

@author: hienpham
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n - 1 - 2*i):
                temp = matrix[i][i + j]
                matrix[i][i + j] = matrix[n - 1 - i - j][i]
                matrix[n - 1 - i - j][i] = matrix[n - 1 - i][n - 1 - i - j]
                matrix[n - 1 - i][n - 1 - i - j] = matrix[i + j][n - 1 - i]
                matrix[i + j][n - 1 - i] = temp