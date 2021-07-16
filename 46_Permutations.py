#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:59:48 2021

@author: hienpham
"""
class Solution:
    def dp(self, arr, path, ans):
        if not arr:
            ans.append(path)
            return
        
        for i in range(len(arr)):
            self.dp(arr[:i] + arr[i+1:], path + [arr[i]], ans)
        
    def permute(self, nums):
        ans = []
        self.dp(nums, [], ans)
        return ans


nums = [1, 2, 3]
ans = Solution().permute(nums)
        