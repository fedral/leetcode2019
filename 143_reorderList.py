# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:51:10 2019

@author: fed
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        p = head
        l = []
        while p:
            l.append(p)
            p = p.next
            
        n = len(l)
        for i in range(n//2):
            l[i].next = l[n-i-1]
            l[n-i-1].next = l[i+1]
            
        if n > 0:
            l[n//2].next = None
            
            
            
            
            
            
            