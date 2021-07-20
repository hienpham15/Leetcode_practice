#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:58:14 2021

@author: hienpham
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        n = len(digits)
        i = n - 1
        carry = 1
        
        while i >= 0:
            temp = digits[i] + carry
            digits[i] = temp%10
            carry = temp//10
            i -= 1
            
        if carry == 1:
            digits.insert(0, carry)
            
        return digits