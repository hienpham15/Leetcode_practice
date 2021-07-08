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
    
    
    def searchRange_v2(self, nums, target):
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l = search(lo, mid)
                r = search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
    

nums = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 10]
target = 8
ans = Solution().searchRange(nums, target)
ans2 = Solution().searchRange_v2(nums, target)