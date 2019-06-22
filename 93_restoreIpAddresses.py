# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:00:23 2019

@author: fed
"""



class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        res = []
		# 判读是否满足ip的条件
        def helper(tmp):
            if not tmp or (tmp[0] == "0" and len(tmp) > 1) or int(tmp) > 255:
                return False
            return True
		# 三个循环,把数字分成四份
        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        # print(tmp1, tmp2, tmp3, tmp4)

                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res




        # dfs
        
        leng=len(s)
        res=[]
        def dfs(s,temp,count):
            if count==3:
                if len(s)==1 or (len(s)>1 and int(s[0])!=0 and int(s[:])<256):
                    temp+=s[:]
                    res.append(temp)
                return
            for i in range(1,len(s)):
                if i>3 or int(s[:i])>256 or (i>1 and int(s[0])==0):
                    continue
                dfs(s[i:],temp+s[:i]+".",count+1)
        dfs(s,"",0)
        return res







