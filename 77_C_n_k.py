# -*- coding: utf-8 -*-
"""
Created on Wed May 29 05:58:40 2019

@author: fed
"""

def combine( n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    
    if k>n or k==0:
        return []
    if k==1:
        return [[i] for i in range(1,n+1)]
    if k==n:
        return [[i for i in range(1,n+1)]]
    #从前 n-1 个数提取 k 个组合
    answer = combine(n-1,k) 
    #从前 n-1 个数提取 k-1 个组合，补上 n
    for item in combine(n-1,k-1):
        item.append(n) #
        answer.append(item)
    
    return answer   


combine(10,4)