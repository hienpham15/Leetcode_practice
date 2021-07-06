#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:28:18 2021

@author: hienpham
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if divisor == 0:
            return 2**31 - 1
        
        res = 0
        
        a = abs(dividend)
        b = abs(divisor)
        
        for i in range(31, -1, -1):
            if (a >> i) - b >= 0:
                res += 1 << i
                a -= b << i 
        
        
        ans = res if (dividend > 0) == (divisor > 0) else -res
        
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans


dividend = 7
divisor = -3
ans = Solution().divide(dividend, divisor)