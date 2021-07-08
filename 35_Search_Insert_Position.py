#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:22:22 2021

@author: hienpham
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                return mid 
        
        return mid + 1
    
nums = [1, 3, 5, 6]
target = 7
ans = Solution().searchInsert(nums, target)
