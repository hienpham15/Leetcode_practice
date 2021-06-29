#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:16:12 2021

@author: hienpham
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 'false'
        elif x == 0:
            return 'true'
        elif x > 0:
            x_str = str(x)
            if x_str == x_str[::-1]:
                return 'true'
            else:
                return 'false'
            
            
x = -121
ans = Solution().isPalindrome(x)