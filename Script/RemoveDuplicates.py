# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:25:34 2017

@author: qiangwennorge
"""
'''
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        newpointer = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[newpointer]:
                newpointer += 1
                nums[newpointer] = nums[i]
        
        return newpointer + 1
        
        
f = Solution()
print f.removeDuplicates([])
