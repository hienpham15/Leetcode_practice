#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:10:24 2021

@author: hienpham
"""
class Solution:
    def combine(self, numpad, digit, comb):
        ans = []
        a = numpad[int(digit)]
        if not comb:
            return a
        
        for i in range(len(comb)):
            for j in range(len(a)):
                ans.append(comb[i] + a[j])
        
        return ans
                
        
    def letterCombinations(self, digits: str):
        numpad = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5:['j', 'k', 'l'], \
                  6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        
        if not digits:
            return []
        
        if len(digits) == 1:
            return numpad[int(digits[0])]
        
        comb = []
        for i in range(len(digits)):
            comb = self.combine(numpad, digits[i], comb)
        
        return comb