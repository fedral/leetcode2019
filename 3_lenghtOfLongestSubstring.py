#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:11:52 2019

@author: fedral1992
"""

class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        '''
        #1 暴力解法 O(N) TLE
        '''
        res=0
        for i,ss in enumerate(s):
            tmp=ss
            for j in range(i+1,len(s)):
                if s[j] not in tmp:
                    tmp+=s[j]
                else:
                    break
                
            res=max(res,len(tmp))
        return res
            
        
        
    def solution2(self, s):
        l=len(s)
        
        '''
        #2 滑动窗口法
        逐个位置考察，维护一个最长的连续不重复的字串
        如果不重复，添加
        如果重复，留下不包含重复字符的右半部分
        '''
        res=0
        tmp=""
        for i in range(l):
            if s[i] not in tmp:
                tmp+=s[i]
                res=max(res,len(tmp))
            else:
                tmp=tmp[tmp.index(s[i])+1:]+s[i]  
                # string.index() O(1) ????
                # 建表字符表 记录下下标位置 保证O(1)
        return res
                
            
            
        
    def solution3(self,s):        
        '''
        #3 对#2的优化：直接利用小标，记录不重复字串 左侧的位置。
        '''
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans        
        
        
        
        

    
          
        
        