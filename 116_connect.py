# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:33:52 2019

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
        
        if root.left:
            root.left.next = root.right          
            if root.next:                       
                root.right.next = root.next.left 
                
        self.connect(root.left)
        self.connect(root.right)
        return root
    

        '''
        using quene
        '''
        
        if not root: 
            return root
        queue = [root]
        
        while(queue): 
            node_pre = None
            for i in range(len(queue)):
                node = queue.pop(0)
                if node_pre: 
                    node_pre.next = node
                node_pre = node
                
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        return root    
    
