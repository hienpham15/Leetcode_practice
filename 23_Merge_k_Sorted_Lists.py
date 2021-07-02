#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 01:28:07 2021

@author: hienpham
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        dummy = ans
        p1 = l1
        p2 = l2
        while p1 is not None or p2 is not None:
            
            if p1 is None:
                dummy.next = p2
                return ans.next
            elif p2 is None:
                dummy.next = p1
                return ans.next
            
            if p1.val <= p2.val:
                val = p1.val
                p1 = p1.next
            else:
                val = p2.val
                p2 = p2.next
                
            dummy.next = ListNode(val)
            dummy = dummy.next
            
        return ans.next
    
    
    def mergeKLists(self, lists) -> ListNode:
        
        interval = 1
        
        n_list = len(lists)
        while interval < n_list:
            for i in range(0, n_list - interval, interval*2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            
            interval *= 2
            
        return lists[0] if n_list != 0 else None