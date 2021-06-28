#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:06:47 2021

@author: hienpham
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        
        i, j = 0, 0
        d = {}

        while j <= len(s) - 1:
            window = s[i:j+1]
        
            if j + 1 == len(s):
                window = s[i:len(s)]
                d.update({len(window): window})
                return max(d)
            if s[j+1] not in window:
                j += 1
                
            else:
                i += window.index(s[j+1]) + 1
                d.update({len(window): window})
        return max(d)
    
s = "abcabcbb"
ans = Solution().lengthOfLongestSubstring(s)