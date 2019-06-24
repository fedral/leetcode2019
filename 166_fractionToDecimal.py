# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:12:58 2019

@author: fed
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
       
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        m, n = divmod(numerator, denominator)
        int_part = str(m)
        if not n:
            return sign + int_part
        
        decimal_part = []
        dic = {}
        i = 0
        while n and n not in dic:
            dic[n] = i
            i += 1
            m, n = divmod(n * 10, denominator)
            decimal_part.append(str(m))
        if n:
            decimal_part.insert(dic[n], '(')
            decimal_part.append(')')
            
        return sign + int_part + '.' + ''.join(decimal_part)
        
        
        
    
    
    
    