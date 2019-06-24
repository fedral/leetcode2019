# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:21:28 2019

@author: fed
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:return
        if root.left and root.right:
            root.left.next=root.right
        
        root_right_or_left=root.right if root.right else root.left
        rrol=root_right_or_left
        p=root.next
        while rrol and p:
            if p.left:
                rrol.next=p.left
                break
            elif p.right:
                rrol.next=p.right
                break
            else:
                p=p.next
                   
            
        self.connect(root.right)
        self.connect(root.left)
        return root
    
    
    
from Queue import Queue
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return None
        q = Queue()
        q.put(root)
        
        while 1:
            q2 = Queue()
            while not q.empty():
                node = q.get()
                if not q.empty():
                    node.next = q.queue[0]
                
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            q = q2
            if q2.empty(): break
        
        return root  