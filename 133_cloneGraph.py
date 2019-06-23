# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:04:07 2019

@author: fed
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        def dfs(old):
            if old not in d:
                # 每遍历一个节点就创建一个它的副本到哈希表
                d[old] = new = Node(old.val, None)
                # 当所有节点进入哈希表之时开始回溯，修改邻居
                new.neighbors = [*map(dfs, old.neighbors)]
            return d[old]
        
        return dfs(node) 
    
    
    
    