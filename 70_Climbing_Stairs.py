#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:00:16 2021

@author: hienpham
"""
class Solution:
    def dp(self, step, n, d):
        if step == 0:
            return 1
        if step < 0:
            return 0
        
        if step in d:
            return d[step]
        
        d[step] = self.dp(step - 1, n, d) + self.dp(step - 2, n, d)
        return d[step]
    
    
    def climbStairs(self, n: int) -> int:
        d = {}
        ans = self.dp(n, n, d)
        return ans