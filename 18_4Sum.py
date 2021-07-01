#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:12:10 2021

@author: hienpham
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                d ={}
                
                for k in range(j+1, len(nums)):
                    rem = target - (nums[k] + nums[j] + nums[i])
                    if rem in d:
                        quad = [nums[i], nums[j], nums[k], rem]
                        if quad not in quads:
                            quads.append(quad)
                    else:
                        d[nums[k]] = k
                        
        return quads