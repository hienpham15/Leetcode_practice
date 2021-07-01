#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:41:00 2021

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
    
def list2link(arr):
    head = ListNode()
    temp = head
    
    for val in arr:
        temp.next = ListNode(val)
        temp = temp.next
    
    return head.next

arr1 = []
arr2 = []

l1 = list2link(arr1)
l2 = list2link(arr2)

ans = Solution().mergeTwoLists(l1, l2)
            
        