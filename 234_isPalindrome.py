# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:30:59 2019

@author: fed
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next and head:
            return True
        
        arr=[]
        while head:
            arr+=[head.val]
            head=head.next
        l=len(arr)
        return arr[0:l//2] == arr[l//2+l%2:][::-1]
        
    
    
    