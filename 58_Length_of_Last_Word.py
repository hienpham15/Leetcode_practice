#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:28:29 2021

@author: hienpham
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        p2 = len(s) - 1
        
        while p2 > 0 and s[p2] == ' ': p2 -= 1
        
        p1 = p2
        
        while p1 >= 0 and s[p1] != ' ': p1 -= 1
        
        
        return p2 - p1