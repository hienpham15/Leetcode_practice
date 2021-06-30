#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:00:21 2021

@author: hienpham
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        len_h = len(height)
        i = 0
        j = len_h - 1
        
        max_area = 0
        while i < j:
            d = j - i
            if height[i] <= height[j]:
                l = height[i]
                i += 1
            else:
                l = height[j]
                j -= 1
            max_area = l*d if l*d > max_area else max_area
            
        return max_area