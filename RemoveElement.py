# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:27:09 2017

@author: qiangwennorge
"""

'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

    Try two pointers.
    Did you use the property of "the order of elements can be changed"?
    What happens when the elements to remove are rare?
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while (nums.count(val)!=0):
            nums.remove(val)
        
        return len(nums)
            
        
f = Solution()
print f.removeElement([4,5],4)
