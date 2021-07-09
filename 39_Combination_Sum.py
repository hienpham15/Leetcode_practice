#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 00:22:48 2021

@author: hienpham
"""

class Solution:
    def combinationSum(self, candidates, target: int):
        ans = set()
        candidates = sorted(candidates)
        def dp(target, candidates, path, ans):
            for i in range(len(candidates)):
                rem = target - candidates[i]
                
                if rem > 0:
                    dp(rem, candidates, path + [candidates[i]], ans)
                elif rem == 0:
                    ans.add(tuple(sorted(path + [candidates[i]])))
                    return
                else:
                    return
                #self.path += dp(rem, d)
            
        dp(target, candidates, [], ans)
        return list(list(x) for x in ans)
        
    
    def combinationSum_v2(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
        
candidates = [2, 3, 6, 7]
target = 7
ans = Solution().combinationSum(candidates, target)            
       
            
            
        