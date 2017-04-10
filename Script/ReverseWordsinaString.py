# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:21:46 2017

@author: qiangwennorge
"""

'''
 Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the". 
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        wordlist = s.split() 
        reverselist = wordlist[::-1]
        result = ' '.join(reverselist)
        return result
        
        
f = Solution()
s = "the sky is      blue"
s = ''
s = "The,sky,is.blue"
print f.reverseWords(s)        