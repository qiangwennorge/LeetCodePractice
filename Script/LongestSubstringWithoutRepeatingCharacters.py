# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:14:48 2017

@author: w00731539
"""

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        inputdict = {}
        result = 0
        start = 0
        for i, ch in enumerate(s):
            if ch in inputdict:
                result = max(result, i - start)
                start = max(start , inputdict[ch] + 1)
            inputdict[ch] = i
        
        result = max(result, len(s) - start)
        
        return result
    
f = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print f.lengthOfLongestSubstring(s3) 
        
