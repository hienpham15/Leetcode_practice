#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:02:31 2021

@author: hienpham
"""
class Solution:
    def dp(self, i, j, s, p):
        if i > len(s) - 1 and j > len(p) - 1:
            return True
        if i > len(s) - 1 and j == len(p) - 1 and p[j] == "*":
            return True
        elif i > len(s) - 1:
            return False
        elif j > len(p) - 1:
            return False
        
        if p[j] in {s[i], "?"}:
            ans = self.dp(i+1, j+1, s ,p)
        elif p[j] == "*":
            ans = self.dp(i, j+1, s, p) or self.dp(i+1, j, s, p)
        else:
            return False
        return ans
        
    def isMatch(self, s: str, p: str) -> bool:
        return self.dp(0, 0, s, p)
    
s = ''
p = '*****'
ans = Solution().isMatch(s, p)
        