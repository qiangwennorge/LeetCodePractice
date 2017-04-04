# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 09:20:34 2017

@author: qiangwennorge
"""
'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
           inputstr = str(x) 
           reversestr = inputstr[::-1]
           outputint = int(reversestr)
           if outputint <= 2**31:
               output = outputint
           else:
               output = 0
        else:
            inputstr = str(abs(x))
            reversestr = inputstr[::-1]
            outputint = int(reversestr)
            if outputint <= 2**31:
                output = - outputint
            else:
                output = 0
        return output


f = Solution()
print f.reverse(10000003)
