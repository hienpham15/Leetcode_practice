#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:30:41 2021

@author: hienpham
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d = {}
        
        def dp(i, j):
            if (i, j) in d:
                return d[(i, j)]
            
            if i >= len(s) and j >= len(p):
                return True
            elif j >= len(p):
                return False 
            
            match = i < len(s) and p[j] in {s[i], '.'}
            
            if j + 1 < len(p) and p[j + 1] == "*":
                ans = dp(i, j+2) or (match and dp(i+1, j))
            else:
                ans = match and dp(i+1, j+1)

            d[(i, j)] = ans
            return ans
        return dp(0, 0)
                