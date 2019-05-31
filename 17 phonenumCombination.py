# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:30:24 2019

@author: fed
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output     
'''
执行用时 : 16 ms, 在Letter Combinations of a Phone Number的Python提交中击败了99.79% 的用户
内存消耗 : 11.7 MB, 在Letter Combinations of a Phone Number的Python提交中击败了34.43% 的用户
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        
        if not digits: return []
        ls1 = ['']
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
        return ls1
    
    
'''
执行用时 : 48 ms, 在Letter Combinations of a Phone Number的Python3提交中击败了92.78% 的用户
内存消耗 : 13.1 MB, 在Letter Combinations of a Phone Number的Python3提交中击败了63.04% 的用户
'''


































    