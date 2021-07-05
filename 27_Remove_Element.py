#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:50:55 2021

@author: hienpham
"""
class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)
    
nums = [3, 2, 2, 3]
val = 3
ans = Solution().removeElement(nums, val)