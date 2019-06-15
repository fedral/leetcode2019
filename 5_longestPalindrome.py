# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 09:40:52 2019

@author: fed
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 0:
            return ''

        # 至少就是 1
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub

        return longest_palindrome_str

    def __center_spread(self, s, size, left, right):
        l = left
        r = right
        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1














