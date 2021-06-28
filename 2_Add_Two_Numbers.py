#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:27:55 2021

@author: hienpham
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        
        ans = ListNode()
        temp = ans
        
        carry = 0
        
        def add(ans, temp, l1, l2, carry):
            while (l1 is not None) or (l2 is not None) or carry:
            
                if l1 is None:
                    l1 = ListNode()
                if l2 is None:
                    l2 = ListNode()
            
            
                val = (l1.val + l2.val + carry)%10 
                temp.next = ListNode(val)
                carry = (l1.val + l2.val + carry)//10
                
                l1 = l1.next
                l2 = l2.next
                
                temp = temp.next
            
            return ans.next
        
        return add(ans, temp, l1, l2, carry)
    
    
def list2link(arr):
    ans = ListNode()
    dummy = ans
    for i in range(len(arr)):
        dummy.next = ListNode(arr[i])
        dummy = dummy.next
    return ans.next


def list2link_v2(arr):
    node_list = []
    for val in arr:
        node_list.append(ListNode(val))
    
    for i in range(len(node_list) - 1):
        node_list[i].next = node_list[i+1]
        
    return node_list[0]
    

arr1 = [9, 9, 9, 9]
l1 = list2link(arr1)
arr2 = [9, 9]
l2 = list2link_v2(arr2)

ans = Solution().addTwoNumbers(l1, l2)
