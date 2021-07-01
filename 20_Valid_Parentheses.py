#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:14:00 2021

@author: hienpham
"""
class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        
        d = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if s[i] in {'(', '[', '{'}:
                paren.append(s[i])
            elif s[i] in {')', ']', '}'}:
                if paren:
                    p = paren.pop()
                    if p != d[s[i]]:
                        return False
                else:
                    return False
        
        if len(paren) == 0:
            return True