# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:27:12 2019

@author: fed
"""

from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        
        while queue:
            current_word, level = queue.pop(0)      
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0



## faster
def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    if endWord not in wordList:
        return 0
    l = len(endWord)
    ws = set(wordList)
    
    head = {beginWord}
    tail = {endWord}
    tmp = list('abcdefghijklmnopqrstuvwxyz')
    res = 1
    while head:
        if len(head) > len(tail):
            head, tail = tail, head
        q = set()
        for cur in head:
            for i in range(l):
                for j in tmp:
                    word = cur[:i] + j + cur[i+1:]
                    if word in tail:
                        return res + 1
                    if word in ws:
                        q.add(word)
                        ws.remove(word)
        head = q
        res += 1
    return 0








