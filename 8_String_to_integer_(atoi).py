#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:37:55 2021

@author: hienpham
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        i = 0
        neg = 1
        flag = 0

        num = ''
        
        while i < len(s):
            
            if flag == 1 and not s[i].isdigit():
                break
            if s[i] == '-':
                if flag == 1 or num:
                    break
                else:
                    neg = -1
                flag += 1
            elif s[i] == '+':
                if flag == 1 or num:
                    break
                else:
                    neg = 1
                flag += 1
            
            if s[i] >= '0' and s[i] <= '9':
                num += s[i]
            
            if num and not s[i].isdigit():
                break
            
            if s[i] != ' ' and not s[i].isdigit() and s[i] != '-' and s[i] != '+':
                return 0      

            
            
            i += 1
        
        if num == '':
            return 0
        else:
            int_num = int(num)*neg
        
        if int_num > 2**31 -1:
            return (2**31 - 1) 
        elif int_num < -2**31:
            return (-2**31) 
        else:
            return int_num 
        

s =  " -0012a42"
num = Solution().myAtoi(s)