#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:56:58 2019

@author: fedral1992
"""

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            # 
            
            '''
            # 解题思路
            利用 中位数表示“左右两边数量相等”，转换为一维数组问题；
            利用 有序数组 可以 进行一维数组的二分 降低到 log(n)的时间复杂度；
            
            ## 代码关键点：二分法中 四个点位置判断
            1 B[j-1] > A[i] and A[i-1] > B[j]  不可能出现的情况
                
            2 B[j-1] > A[i] and A[i-1] < B[j]  (第二项 一定成立,可以省略) i太小  
                B[j]>B[j-1]>A[i]>A[i-1]
            3 B[j-1] < A[i] and A[i-1] > B[j]  (第一项一定成立，可以省略)  i太大
                A[i]>A[i-1]>B[j]>B[j-1]
            4 B[j-1] < A[i] and A[i-1] < B[j]
                bingo
            '''
            
            
            if i < m and B[j-1] > A[i]:      #B[j]>B[j-1]>A[i]>A[i-1]
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:    #A[i]>A[i-1]>B[j]>B[j-1]
                # i is too big, must decrease it
                imax = i - 1
            else:                            # B[j-1]< A[i] and  A[i-1] < B[j]
                # i is perfect

                if i == 0: 
                    max_of_left = B[j-1]
                elif j == 0: 
                    max_of_left = A[i-1]
                else: 
                    max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = B[j]
                elif j == n: 
                    min_of_right = A[i]
                else: 
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


    def solution2(self, A, B):
        '''
        次优解法
        O(min(M,N))
        
        '''
        m,n=len(A),len(B)
        mergedlist =[]
        while A and B:
            if A[0]<B[0]:
                mergedlist+=[A.pop(0)]
            else:
                mergedlist+=[B.pop(0)]
        if not A:
            mergedlist+=B
        if not B:
            mergedlist+=A
        
        if (m+n)%2 == 0:
            return sum(mergedlist[(m+n)//2-1:(m+n)//2+1])/2.0
        else:
            return mergedlist[(m+n)//2]
                
                
        
        
        
        





