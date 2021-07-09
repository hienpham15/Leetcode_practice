#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 03:18:40 2021

@author: hienpham

"""
class Solution:
    def combinationSum(self, candidates, target: int):
        ans = set()
        candidates = sorted(candidates)
        def dp(target, candidates, path, ans, idx):
            
            for i in range(idx, len(candidates)):
                rem = target - candidates[i]
                
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                
                if rem > 0:
                    dp(rem, candidates, path + [candidates[i]], ans, i + 1)
                elif rem == 0:
                    ans.add(tuple(sorted(path + [candidates[i]])))
                    return
                else:
                    return
        dp(target, candidates, [], ans, 0)
        return list(list(x) for x in ans)
        
    
    def combinationSum_v2(self, candidates, target):
        ret = []
        candidates.sort()
        self.dfs(candidates, target, [], ret, 0)
        return ret
    
    
    def dfs(self, nums, target, path, ret, idx):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], path+[nums[i]], ret, i + 1)
        
candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 25

ans = Solution().combinationSum(candidates, target)            