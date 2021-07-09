#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 00:22:48 2021

@author: hienpham
"""

class Solution:
    def combinationSum(self, candidates, target: int):
        ans = set()
        path = []
        candidates = sorted(candidates)
        def dp(target, candidates, path, ans):
            for i in range(len(candidates)):
                rem = target - candidates[i]
                
                if rem > 0:
                    path += [candidates[i]]
                    dp(rem, candidates, path, ans)
                elif rem == 0:
                    ans.add(tuple(sorted(path + [candidates[i]])))
                    return
                else:
                    return
                path.pop()
                #self.path += dp(rem, d)
            
        dp(target, candidates, path, ans)
        return list(list(x) for x in ans)
        
        
        
candidates = [2,7,6,3,5,1]
target = 9
ans = Solution().combinationSum(candidates, target)            
       
            
            
        