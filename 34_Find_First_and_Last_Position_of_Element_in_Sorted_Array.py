#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:11:19 2021

@author: hienpham
"""
class Solution:
    def searchRange(self, nums, target: int):
        first, last = -1, -1
        
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low + high)//2
            
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                first, last = mid, mid
                
                while first > 0:
                    if nums[first-1] == target:
                        first -= 1
                    else:
                        break
                
                while last < len(nums) - 1:
                    if nums[last+1] == target:
                        last += 1
                    else:
                        break
                        
                return [first, last]
                
        return [first, last]
    

nums = [1, 8, 8]
target = 8
ans = Solution().searchRange(nums, target)