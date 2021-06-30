#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:28:26 2021

@author: hienpham
"""
class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        
        for i in range(len(nums) - 1):
            hmap = {}
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                num_k = target - nums[j]
                if num_k in hmap:
                    triplet = [nums[i], nums[j], num_k]
                    if triplet not in ans:
                        ans.append(triplet)
                else:
                    hmap[nums[j]] = j
        return ans

nums = [0]    
ans = Solution().threeSum(nums)
                
            