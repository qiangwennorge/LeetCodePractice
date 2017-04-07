# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:22:28 2017

@author: qiangwennorge
"""

'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        output = 0
        for i in range(0,len(s)-1):
            if romandict[s[i]] < romandict[s[i+1]]:
                output -= romandict[s[i]]
            else:
                output += romandict[s[i]]                
        return output + romandict[s[-1]]

f = Solution()
print f.romanToInt('MCDXLVI')
            
        
