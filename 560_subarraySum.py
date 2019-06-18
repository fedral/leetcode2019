# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:52:59 2019

@author: fed
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        
        #O(n）
        ht={}
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                key = sum(nums[i:j+1])
                ht[key] = ht.get(key,0)+1
        if k in ht:
            return ht[k]
        else:
            return 0
        
        
        # O_N hash right way 
        m = {0:1}
        sumN = 0
        count=0
        for i in range( len(nums) ):
            sumN +=nums[i]
            count+=m.get(sumN-k,0)
            m[sumN]=m.get(sumN,0)+1
        return count
                
    
'''

执行用时 :
120 ms
, 在所有 Python 提交中击败了
93.62%
的用户
内存消耗 :
13.9 MB
, 在所有 Python 提交中击败了
21.67%
的用户
'''

    
    