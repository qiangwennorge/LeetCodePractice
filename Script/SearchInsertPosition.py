# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 11:11:16 2017

@author: qiangwennorge
"""

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        nums.sort()
        result = 0
        length = len(nums)
            
        if length == 2:
            if target > nums[0] and target <= nums[1]:
                result = 1
            elif target <= nums[0]:
                result = 0
            else:
                result = 2
        else:
            for i in range(0, length - 1):
                if target > nums[i] and target <= nums[i+1]:
                    result = i + 1
                elif target == nums[i]:
                    result = i
                    
            if target == nums[-1]:
                result = length - 1
            elif target > nums[-1]:
                result = length 
        return result    

f = Solution()
print f.searchInsert([1,3,5],4)
