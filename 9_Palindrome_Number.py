#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:16:12 2021

@author: hienpham
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x > 0:
            x_str = str(x)
            if x_str == x_str[::-1]:
                return True
            else:
                return False
            
            
    def isPalindrome_v2(self, x: int) -> bool:
        
        if x < 0 or (x%10 == 0 and x !=0):
            return False
        elif x == 0:
            return True
        
        revert_num = 0
        
        while x > revert_num:
            digit = x % 10
            x = x//10
            
            revert_num = revert_num*10 + digit 
        
        if x == revert_num or x == revert_num//10:
            return True
        else:
            return False
            
        
    
            
x = -121
ans = Solution().isPalindrome(x)