#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:32:49 2021

@author: hienpham
"""
class Solution:
    def dp(self, arr, path, ans):
        if not arr:
            ans.add(tuple(path))
            return
        
        for i in range(len(arr)):
            self.dp(arr[:i] + arr[i+1:], path + [arr[i]], ans)
        
    def permuteUnique(self, nums):
        ans = set()
        self.dp(nums, [], ans)
        return list(list(x) for x in ans)
    

nums = [1, 1, 3]
ans = Solution().permute(nums)
    
