#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:27:15 2021

@author: hienpham
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if intervals:
            if newInterval[0] < intervals[0][0]:
                ans = [newInterval]
            else:
                ans = [intervals[0]]
        else:
            return [newInterval]
        
        l_m, r_m = newInterval
        
        i = 0
        j = 0
        
        while i < len(intervals):
            l, r = intervals[i]
            if r_m < l:
                ans += intervals[i:]
                return ans
            print(ans)
            
            if l_m > r:
            
                if i+1 < len(intervals):
                    if r_m < intervals[i+1][0]:
                        ans += [newInterval]
                    else:
                        #ans += [[l_m,  intervals[i+1][1]]]
                        ans += [intervals[i+1]]
                    j += 1
                else:
                    ans += [newInterval]
                
            else:
                if l_m < l:
                    ans[j][0] = l_m
                else:
                    l_m = l
                               
                if r_m > r:
                    ans[j][1] = r_m  
                else:
                    ans[j][1] = r
                  
            i += 1
            
        return ans