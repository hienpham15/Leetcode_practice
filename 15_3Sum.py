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
    
    
    def threeSum_v2(self, nums):
        #split into negatives, zeros, and positives

        nums.sort()
        ans = []
        
        poss = [val for val in nums if val > 0]
        negs = [val for val in nums if val < 0]
        zeros = [val for val in nums if val == 0]
        
        N, P = set(negs), set(poss)
        
        if zeros:
            for val in N:
                if -val in P:
                    triplet = [val, 0, -val]
                    if triplet not in ans:
                        ans.append(triplet)
        
        if len(zeros) >= 3:
            ans.append(triplet)
            
        
        for i in range(len(negs) - 1):
            for j in range(i+1, len(negs)):
                negs_k = -(negs[i] + negs[j])
                if negs_k in N:
                    triplet = [negs[i], negs[j], negs_k]
                    if triplet not in ans:
                        ans.append(triplet)
        
        for i in range(len(poss) - 1):
            for j in range(i+1, len(poss)):
                poss_k = -(poss[i] + poss[j])
                if poss_k in N:
                    triplet = [poss[i], poss[j], poss_k]
                    if triplet not in ans:
                        ans.append(triplet)
        return ans
        

nums = [0]    
ans = Solution().threeSum(nums)
                
            