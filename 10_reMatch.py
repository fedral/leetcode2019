# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:08:48 2019

@author: fed
"""


class Solution(object):
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not pattern: 
            return not text

        first = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or first and self.isMatch(text[1:], pattern)
        else:
            return first and self.isMatch(text[1:], pattern[1:])





