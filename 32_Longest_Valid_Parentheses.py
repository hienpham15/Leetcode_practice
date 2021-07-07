#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:27:30 2021

@author: hienpham
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if right > left:
                left, right = 0, 0
            elif left == right:
                longest = 2*left if 2*left > longest else longest
        
        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            
            if right < left:
                left, right = 0, 0
            elif right == left:
                longest = right*2 if right*2 > longest else longest
        
        return longest
        