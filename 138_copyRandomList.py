# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:58:58 2019

@author: fed
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cur, m = head, {}
        while cur:
            m[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head

        while cur:
            if cur.next:
                m[cur].next = m[cur.next]
            else:
                m[cur].next = None
            if cur.random:
                m[cur].random = m[cur.random]
            cur = cur.next
        return m[head]
    
    
    
    
        # sol 2
        nodeDict = {}
        dummy = Node(0, None, None)
        nodeDict[head] = dummy
        newHead, pointer = dummy, head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            nodeDict[pointer] = node
            newHead.next = node
            newHead, pointer = newHead.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]
            pointer = pointer.next
        return dummy.next