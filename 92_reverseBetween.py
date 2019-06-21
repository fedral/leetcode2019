# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:16:37 2019

@author: fed
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        a = head
        b = head
        for i in range(m-1):
            if i == m-2:
                b = a
            a = a.next
        p = a.next
        q = a
        c = a
        for i in range(n-m):
            a = p
            p = p.next
            a.next = q
            q = a
            
        if m!=1:
            b.next = a
            c.next = p
        else:
            c.next = p
            head = a
        return head
    
    


    
    