#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:34:15 2021

@author: hienpham
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = {}
        ans = ''
        for i in range(numRows):
            d.update({i + 1: ''})
        
        i = 0
        count = 1
        if len(s) == 1:
            return s
        
        if numRows == 1:
            return s
        
        while i < len(s):
            
            while count < numRows and i < len(s):
                string = d[count] + s[i]
                d.update({count:string})
                count += 1
                i += 1
            
            while count > 1 and i < len(s):
                string = d[count] + s[i]
                d.update({count:string})
                count -= 1
                i += 1
                
        for i in range(len(d)):
            ans += d[i+1]
            
        return ans
    
s = 'AA'
ans = Solution().convert(s, 1)