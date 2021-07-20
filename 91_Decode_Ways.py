#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:05:31 2021

@author: hienpham
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def dp(s):
            if len(s) > 0:
                if s[0] == '0':
                    return 0
        
            if not s or len(s) == 1:
                return 1
        
            if 1 <= int(s[0:2]) <= 26:
                return dp(s[1:]) + dp(s[2:])
            else:
                return dp(s[1:])
        
        return dp(s)
        