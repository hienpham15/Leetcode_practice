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
            
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])
                
            ans += min(left_max, right_max) - height[i]
        return ans
    

    def trap_v2(self, height):
        left = 0
        right = len(height) - 1
        
        left_max = 0
        right_max = 0
        
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                    
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                    
                right -= 1
        return ans
    
    
height = [4, 2, 0, 3, 2, 5]
ans = Solution().trap_v2(height)    