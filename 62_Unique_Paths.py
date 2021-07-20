#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:17:37 2021

@author: hienpham
"""
class Solution:
    def dp(self, m, n, d):
        if m == 0 or n == 0:
            return 1
        
        if m < 0 or n < 0:
            return 0
        
        if (m, n) in d:
            return d[(m, n)]
        
        count = self.dp(m-1, n, d) + self.dp(m, n-1, d)
        d[(m, n)] = count 
        return count
        
    def uniquePaths(self, m: int, n: int) -> int:
        d = {}
        count = self.dp(m-1, n-1, d)
        return count
    

ans = Solution().uniquePaths(3, 7)