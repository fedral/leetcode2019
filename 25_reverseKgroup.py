# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:04:25 2019

@author: fed
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k 
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
    
            if count : 
                p.next = head
                break
            
            while stack:
                p.next = stack.pop()
                p = p.next
            
            p.next = tmp
            head = tmp
        
        return dummy.next

    
'''
执行用时 : 72 ms, 在Reverse Nodes in k-Group的Python提交中击败了15.94% 的用户
内存消耗 : 13.6 MB, 在Reverse Nodes in k-Group的Python提交中击败了22.95% 的用户
'''
    