#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:05:13 2021

@author: hienpham
"""
class Solution:
    def dfs(self, i, j, grid, d):
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        
        if grid[i][j] == 1:
            return 0
        
        if (i, j) in d:
            return d[(i, j)]
        
        d[(i, j)] = self.dfs(i-1, j, grid, d) + self.dfs(i, j-1, grid, d)
        
        return d[(i, j)]
        
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        d = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = self.dfs(m-1, n-1, obstacleGrid, d)
        return ans