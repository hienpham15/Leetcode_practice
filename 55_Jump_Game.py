#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:22:47 2021

@author: hienpham
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left = 0
        right = nums[0]
        
        while right < len(nums) - 1:
            possible_jumps = [i + nums[i] for i in range(left, right+1)]
            left = right + 1
            right = max(possible_jumps)
            
            if left > right:
                return False
            
        return True