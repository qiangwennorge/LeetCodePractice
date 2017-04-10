# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:49:40 2017

@author: qiangwennorge
"""
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        if x[::-1] == x:
            return True
        return False
        
        
f = Solution()
print f.isPalindrome(1001)