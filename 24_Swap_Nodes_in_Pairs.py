#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 01:22:53 2021

@author: hienpham
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        pre = dummy = ListNode(0)
        dummy.next = head
        
        while dummy.next and dummy.next.next:
            p1 = dummy.next
            p2 = p1.next
            
            dummy.next = p2
            p1.next = p2.next
            p2.next = p1
            
            dummy = p1
            
        return pre.next
        
        
        
def list2link(arr):
    head = ListNode()
    temp = head
    
    for val in arr:
        temp.next = ListNode(val)
        temp = temp.next
    
    return head.next

arr = [1, 2, 3, 4]
link = list2link(arr)
ans = Solution().swapPairs(link)