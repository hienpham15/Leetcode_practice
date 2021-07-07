#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:27:30 2021

@author: hienpham
"""
class Solution:
    def find_match(self, nums, p1, val):
        """
        find index of a value in nums that almost equal to val
        """
        arr = [abs(x - val) for x in nums[p1:]]
        idx = p1 + arr.index(min(arr))
        return idx
        

    
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1
        
        i = len(nums) - 1
        
        while i > 0:
            if nums[i - 1] < nums[i]:
                p1 = i
                idx = self.find_match(nums, p1, nums[i - 1])
                nums[i - 1], nums[idx] = nums[idx], nums[i - 1]
                
                temp = nums[i:]
                temp.reverse()
                nums[i:] = temp[:]
                return
            else:
                i -= 1
                
        nums.reverse()
        
nums = [1, 1, 5]
Solution().nextPermutation(nums)
            
            