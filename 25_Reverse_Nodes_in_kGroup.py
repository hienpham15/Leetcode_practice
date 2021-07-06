#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:33:06 2021

@author: hienpham
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
         
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = head
        left = right = head
        
        while True:
            count = 0
            # Go to k-th node
            while right and count < k:
                count += 1
                right = right.next
            
            
            if count == k:
                # Standard reverse link list
                pre = right
                cur = left
                for _ in range(k):
                    nex = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nex
                
                jump.next = pre
                jump = left
                left = right
            else:
                return dummy.next

        

def list2link(arr):
    dummy = head = ListNode(0)
    
    for val in arr:
        dummy.next = ListNode(val)
        dummy = dummy.next
    
    return head.next
    
arr = [1, 2, 3, 4, 5, 6]
k = 5
l = list2link(arr)
ans = Solution().reverseKGroup(l, 5)        