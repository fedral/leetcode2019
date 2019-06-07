# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:16:31 2019

@author: fed
"""


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        newhead = head.next
        head.next = self.swapPairs(head.next.next)
        newhead.next = head
        return newhead
    
    
'''
执行用时 : 20 ms, 在Swap Nodes in Pairs的Python提交中击败了94.50% 的用户
内存消耗 : 11.7 MB, 在Swap Nodes in Pairs的Python提交中击败了40.24% 的用户

'''





