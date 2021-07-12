#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:01:24 2021

@author: hienpham
"""
class Solution:
    def trap(self, height) -> int:
        
        ans = 0
        for i in range(len(height)):
            left_max = 0
            right_max = 0
            
            for j in range(i, 0, -1):
                left_max = max(left_max, height[j])
            
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])
                
            ans += min(left_max, right_max) - height[i]
        return ans
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = Solution().trap(height)    