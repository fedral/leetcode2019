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
            
        
    # solution 3
            if not s or not words:
            return []
            n = len(s)
            k = len(words[0])
            t = len(words) * k
            req = {}
            for w in words:
                req[w] = req[w] + 1 if w in req else 1
            ans = []
            
            for i in xrange( min(k, n - t + 1) ):
                self._findSubstring(i, i, n, k, t, s, req, ans)
            return ans
    
        def _findSubstring(self, l, r, n, k, t, s, req, ans):
            curr = {}
            while r + k <= n:
                w = s[r:r + k]
                r += k
                if w not in req:
                    l = r
                    curr.clear()
                else:
                    curr[w] = curr[w] + 1 if w in curr else 1
                    while curr[w] > req[w]:
                        curr[s[l:l + k]] -= 1
                        l += k
                    if r - l == t:
                        ans.append(l)
    
    
    
    
    
    
    
    