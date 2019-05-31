# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:54:05 2019

@author: fed
"""

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0) return 0;
        int i=0;
        for(int j=1;j<nums.size();j++)
        {
            if(nums[j]!=nums[i])
            {
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
    }
};
            
'''
执行用时 : 24 ms, 在Remove Duplicates from Sorted Array的C++提交中击败了99.61% 的用户
内存消耗 : 10 MB, 在Remove Duplicates from Sorted Array的C++提交中击败了75.10% 的用户

'''



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]: nums.pop(i)
        return len(nums)   
    
'''
执行用时 : 92 ms, 在Remove Duplicates from Sorted Array的Python提交中击败了87.71% 的用户
内存消耗 : 13.5 MB, 在Remove Duplicates from Sorted Array的Python提交中击败了29.85% 的用户
'''








