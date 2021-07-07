#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:44:00 2021

@author: hienpham
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    
    
nums = [-1,0,0,0,0,3,3]
ans = Solution().removeDuplicates(nums)