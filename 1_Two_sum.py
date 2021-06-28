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
            return [i, (i + 1) + nums[(i+1):].index(element)]

def solution1(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def solution2(nums, target):
    hmap = {}
    for i in range(len(nums)):
        element = target - nums[i]
        if element in hmap:
            return [i, hmap[element]]
        else:
            hmap.update({nums[i]:i})


#nums = [2, 5, 5, 11]
#target = 10

#ans = solution1(nums, target)


