#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:59:26 2021

@author: hienpham
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        begin = 0
        end = x
        
        if x == 1:
            return 1
        
        while begin <= end:
            mid = (begin+end)//2
            
            if mid*mid <= x < (mid +1)*(mid+1):
                return mid
            elif x < mid*mid:
                end = mid 
            else:
                begin = mid 