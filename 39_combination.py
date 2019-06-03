# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:31:37 2019

@author: fed
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates = sorted(candidates)
        res=[]
        st=[]
        n,i=len(candidates),0
        while True:
            if target==0:
                res.append([candidates[i] for i in st])
                i=st.pop()
                target+=candidates[i]
                i+=1
            elif i==n or candidates[i]>target:
                if len(st)==0:
                    return res
                i=st.pop()
                target+=candidates[i]
                i+=1
            elif candidates[i]<=target:
                st.append(i)
                target-=candidates[i]
                
'''
执行用时 : 44 ms, 在Combination Sum的Python提交中击败了97.90% 的用户
内存消耗 : 11.7 MB, 在Combination Sum的Python提交中击败了35.36% 的用户
'''



class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def find(output, target):
            if target == 0 and sorted(output) not in res:
                res.append(sorted(output))
                return
            for candidate in candidates:
                new_target = target - candidate
                if new_target >= 0:
                    find(output + [candidate], new_target)
            
        res = []
        find([], target)
        return res
    
    









