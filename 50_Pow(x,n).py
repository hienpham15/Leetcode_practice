#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:38:36 2021

@author: hienpham
"""
class Solution:
    
    def power(self, x, n, hashmap):
        if n == 0:
            return 1
        if n == 1:
            return x
        
        k = abs(n)//2
        
        if (x, k) in hashmap:
            p_k = hashmap[(x, k)]
        else:
            p_k = self.power(x, k, hashmap)
            hashmap[(x ,k)] = p_k

        if abs(n)%2 == 0:
            powah = p_k * p_k
        else:
            powah = p_k * p_k * x
            
        return powah
            
     
    
    def myPow(self, x: float, n: int) -> float:
        
        hashmap = {}
        
        powah = self.power(x, n, hashmap)
        
        if n > 0:
            return powah
        else:
            return 1/powah
        
        
x = 2
n = -2
ans = Solution().myPow(x, n)
        
        
        