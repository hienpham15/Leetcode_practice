#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:52:21 2021

@author: hienpham
"""
class Solution:
    def check_string(self, words, i, window):
        check_set = words[:]
        check_set.remove(words[i])
        
        for word in check_set:
            if word not in window:
                return False
            else:
                window = window.replace(word, '', 1)
            
        return True
        
    
    def findSubstring(self, s: str, words):
        sub_total_len = 0
        d = {}
        ans = []
        
        for sub_s in words:
            sub_total_len += len(sub_s)
        
        for i, word in enumerate(words):
            a = [i for i in range(len(s)) if s.find(word, i) == i]
            d.update({i:a})
            
        
        for i in range(len(d)):
            pos = d[i]
            word_len = len(words[i])
            for idx in pos:
                window = s[idx + word_len:idx + sub_total_len]
                if self.check_string(words, i, window):
                    ans.append(idx)
        
       
        
        return list(set(ans))

s = "abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabaccaacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa"
words = ["cac","aaa","aba","aab","abc"]

ans = Solution().findSubstring(s, words)
                
            
        