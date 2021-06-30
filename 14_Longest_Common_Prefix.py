#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:52:11 2021

@author: hienpham
"""
class Solution:
    def lcp(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        i, j = 0, 0
        ans = '' 
        while i < l1 and j < l2:
            if s1[i] == s2 [j]:
                ans += s1[i]
                i += 1
                j += 1
            else:
                return ans
        return ans        
        
    
    def longestCommonPrefix(self, strs) -> str:
        list_len = len(strs)
        
        if list_len == 1: 
            return strs[0]
        
        lcp_ans = self.lcp(strs[0], strs[1])
        i = 2
        
        if lcp_ans == '':
            return ''
        
        while i < list_len:
            lcp_check = self.lcp(lcp_ans, strs[i])
            
            if lcp_check == '':
                return ''
            else:
                lcp_ans = lcp_check
                i += 1
                
        return lcp_ans
    
strs = ["dog","racecar","car"]
ans = Solution().longestCommonPrefix(strs)