#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:24:46 2021

@author: hienpham
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        ans = [intervals[0]]
        
        i = 1
        j = 0
        
        while i < len(intervals):
            l, r = intervals[i]
            l_c, r_c = ans[j]
            
            if l <= r_c:
                if r > r_c:
                    ans[j][1] = r
            else:
                ans += [intervals[i]]
                j += 1
            
            i += 1
            
        return ans