#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 20:41:10 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def bin_search(a, arr):
    if len(arr) == 1 and a != arr[0]:
        return False
    
    if a > arr[len(arr)//2]:
        return bin_search(a, arr[len(arr)//2:])
    elif a < arr[len(arr)//2]:
        return bin_search(a, arr[:len(arr)//2])
    elif a == arr[len(arr)//2]:
        return True
    


def func(nums, target):
    for i in range(len(nums)-1):
        element = target - nums[i]
        arr = sorted(nums[(i+1):])
        ans = bin_search(element, arr)
        if ans == True:
            return [i, nums[(i+1):].index(element)]

nums = [3, 2, 4]
target = 6

ans = func(nums, target)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, k = [int(i) for i in parse_input().split()]
        multiset = parse_input()
        arr = [int(i) for i in parse_input().split()]
        print(func(multiset, k))
        
if __name__ == "__main__":
    main()