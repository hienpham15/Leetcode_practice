#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:56:01 2021

@author: hienpham
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1