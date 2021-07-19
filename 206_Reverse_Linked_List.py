#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:31:03 2021

@author: hienpham
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        p1 = None
        p2 = head
        
        while p2 is not None:
            rem = p2.next
            p2.next = p1
            
            p1 = p2
            p2 = rem
        
        return p1