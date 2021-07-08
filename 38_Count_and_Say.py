#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:39:09 2021

@author: hienpham
"""
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        ans = ''
        
        a = self.countAndSay(n-1)
        for k, group in itertools.groupby(a):
            ans += str(len(list(group))) + str(k)
         
        return ans
        
n = 5
ans = Solution().countAndSay(n)
    