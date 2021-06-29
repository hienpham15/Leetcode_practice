#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:52:35 2021

@author: hienpham
"""
class Solution:
    def reverse(self, x: int) -> int:
        
        
        if x < 0:
            neg = True
            x = abs(x)
        else:
            neg = False

        rev_num = 0
        
        while x!= 0:
            digit = x % 10
            x = x//10
            
            rev_num = rev_num*10 + digit
            
        if neg:
            rev_num = rev_num * -1
            
        if rev_num > 2**31 - 1 or rev_num < -2**31:
            return 0
        return rev_num
            
            
a = -12345600
ans = Solution().reverse(a)       