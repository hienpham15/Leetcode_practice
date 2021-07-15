#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:26:07 2021

@author: hienpham
"""
class Solution:
    
    def dp(self, idx, nums, path, d):
        
        if idx == len(nums) - 1:
            n_step = len(path)
            d.update({n_step:path})
            return
        elif idx > len(nums) - 1:
            return
        
        
        max_step = nums[idx]
        
        for i in range(max_step, 0, -1):
            self.dp(idx + i, nums, path + [i], d)
        
        return
        
    
    def jump(self, nums) -> int:
        d = {}
        
        self.dp(0, nums, [], d)
        return min(d)
    
nums = [2, 1]
ans = Solution().jump(nums)