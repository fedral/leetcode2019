# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:51:09 2019

@author: fed
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxx= 0
        now = 0
        while now <= maxx:
            maxx = max(now+nums[now],maxx)
            now += 1
            if maxx >= len(nums)-1:
                return True
        return False
    
    
'''

执行用时 : 100 ms, 在Jump Game的Python提交中击败了86.63% 的用户
内存消耗 : 13.3 MB, 在Jump Game的Python提交中击败了44.08% 的用户
'''