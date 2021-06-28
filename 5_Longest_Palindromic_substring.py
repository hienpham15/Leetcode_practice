#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:12:05 2021

@author: hienpham
"""
class Solution:
    def isPalindrome(self, string):
        if string == string[::-1]:
            return True
        else:
            return False
        
    def longestPalindrome(self, s: str) -> str:
        #
        start = 0
        
        max_length = 1 
        begin = 0
        end = 0
        
        #One by one consider every character as center point of even and length palindromes
        for i in range(1, len(s)):
            
            # Find the longest even length palindrome with center points at i-1 and i
            begin = i - 1
            end = i
            while begin >= 0 and end < len(s) and s[begin] == s[end]:
                if end - begin + 1 > max_length:
                    start = begin
                    max_length = end - begin + 1
                
                begin -= 1
                end += 1    
            
            # Find the longest odd length palindrome with center points at i   
            begin = i - 1
            end = i +1
            while begin >= 0 and end < len(s) and s[begin] == s[end]:
                if end - begin + 1 > max_length:
                    start = begin
                    max_length = end - begin + 1
                begin -= 1
                end += 1
        
        return s[start:start+max_length]
            
            
    
    
s = 'cbbd'
ans = Solution().longestPalindrome(s)