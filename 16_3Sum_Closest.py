#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:17:34 2021

@author: hienpham
"""


class Solution:
    def find_id(self, nums, target):
        temp = nums.copy()
        temp.append(target)
        temp.sort()
        idx = temp.index(target)
        
        if idx == len(temp) - 1:
            return idx - 1
        elif idx == 0:
            return 0
        else:
            d_left = abs(target - temp[idx-1])
            d_right = abs(temp[idx + 1] - target)
            
            if d_left > d_right:
                return idx
            else:
                return idx - 1
            
        
    
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        nums_len = len(nums) - 1
        d_min = 2**31
        
        low = 0
        high = nums_len
        #med = self.find_id(nums, target)
        
        for i in range(len(nums)):
            low = i + 1
            high = nums_len
            
            while low < high:
                s = nums[low] + nums[i] + nums[high]
                d = s - target
            
                if d == 0:
                    return s
                elif d > 0:
                    if abs(d) < abs(d_min):
                        d_min = d
                    high -= 1
                elif d < 0:
                    if abs(d) < abs(d_min):
                        d_min = d
                    low += 1
            
        return d_min + target
                
nums = [1,2,4,8,16,32,64,128]
target = 82
ans = Solution().threeSumClosest(nums, target)                
                
        