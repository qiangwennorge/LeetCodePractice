# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:35:54 2017

@author: qiangwennorge
"""

'''
Write a function to find the longest common prefix string amongst an array of strings. 
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        
        if not strs:
            return result

        strlen = [len(item) for item in strs]
        strlen.sort()
        length = 0
        while length < strlen[0]:
            stritem = [item[length] for item in strs]
            if len(set(stritem)) is 1:
                result += stritem[0]
                length += 1
            else:
                break              
        return result
        
        
f = Solution()
strs = ["abca", "abc"]
strs1 =["ac", "ac", "a", "a"]
strs2 = []
print f.longestCommonPrefix(strs2)