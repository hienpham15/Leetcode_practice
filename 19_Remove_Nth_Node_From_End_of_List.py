#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:16:41 2021

@author: hienpham
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        k = 1
        
        while k <= n+1:
            p1 = p1.next
            k += 1
        
        p2 = dummy
        
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
                
        p2.next = p2.next.next    
        return dummy.next

def list2link(arr):
    head = ListNode()
    temp = head
    
    for val in arr:
        temp.next = ListNode(val)
        temp = temp.next
    
    return head.next

arr = [1, 2, 3, 4, 5]
n = 2
link = list2link(arr)

ans = Solution().removeNthFromEnd(link, n)