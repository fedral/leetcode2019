# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:55:52 2019

@author: fed
"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def backtrack(first = 0):
            if first == n:
                if "".join(nums[:]) not in output:
                    output.append( "".join(nums[:]) )
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  
        
        if s=="": 
            return []
        if words == []:
            return []
        
        nums=words
        n = len(nums)
        output = []
        backtrack()  # TLE due to backtracking
        
        res=[]
        l1,l2=len(output[0]),len(s)
        for subs in output:
            for k in range(0,l2-l1+1):
                if subs == s[k:k+l1]:
                    res+=[k]
        return res
    
    
        # solution 2 
        # don't need to enumerate all 
        # two dicts to count usage of words
        if s == "" or words == []:
            return []
        res = []

        wordsdict = {}
        tempwordsdict = {}
        for word in words:
            if word in wordsdict:
                wordsdict[word] += 1
            else:
                wordsdict[word] = 1


        res=[]
        wl = len(words[0])
        ll = len(words)
        rl = ll * wl
        for i in range(len(s) - rl + 1):
            temp = s[i:i + rl]
            tempwordsdict = wordsdict.copy()
            for j in range(ll):
                theword = temp[wl * j: wl * (j + 1)]
                if theword not in tempwordsdict:
                    break
                else:
                    if tempwordsdict[theword] <=0:
                        break
                    else:
                        tempwordsdict[theword] -= 1
                if j == ll - 1:
                    res.append(i)
        return res
            
        
    
    
    
    
    
    
    
    