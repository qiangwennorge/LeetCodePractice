# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:55:56 2017

@author: qiangwennorge
"""
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 

Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = None
        for i in range(0,len(nums)):
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if result is None or abs(sum - target) < abs(result - target):
                    result = sum  
                if sum > target:
                    right -= 1
                else:
                    left += 1
               
        return result
        
f = Solution()
nums = [1,1,1,0,-2,-1,-5]
nums = [0,2,1,-3]
print f.threeSumClosest(nums,1)
        