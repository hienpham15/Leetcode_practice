#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:17:04 2021

@author: hienpham
"""
class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
 
    
n = 3
ans = Solution().generateParenthesis(n)