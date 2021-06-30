#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:06:30 2021

@author: hienpham
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':4, 'V':5, 'IX':9, \
             'X':10, 'XL':40, 'L':50, 'XC':90, \
             'C':100, 'CD':400, 'D':500, 'CM':900, \
             'M':1000}
        
        i = 0
        num = 0
        while i < len(s):
            if s[i] in {'I', 'X', 'C'}:
                num += d[s[i:i+2]] if s[i:i+2] in d else d[s[i]]
                i += 2 if s[i:i+2] in d else 1
            else:
                num += d[s[i]]
                i += 1
        return num
    
s = 'MCMXCIV'
ans = Solution().romanToInt(s)
            
            
                
            
            