#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:02:00 2021

@author: hienpham
"""
class Solution:
           
    def intToRoman(self, num: int) -> str:
        d = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        
        roman = ''
        for key, roman_char in reversed(d.items()):
            roman += (num//key) * roman_char
            num %= key
        return roman