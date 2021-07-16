#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:10:29 2021

@author: hienpham
"""
class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}
        
        for string in strs:
            a = tuple(sorted(string))
            if a in anagram_dict:
                anagram_dict[a].append(string)     
            else:
                anagram_dict[a] = [string]
        
        ans = []
        
        for val in anagram_dict.values():
            ans.append(val)
            
        return ans
    
strs = ["eat","tea","tan","ate","nat","bat"]
ans = Solution().groupAnagrams(strs)