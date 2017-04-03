# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 14:10:01 2017

@author: qiangwennorge
"""

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
'''
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    suitlist = [nums[i],nums[j],nums[k]]
                    if nums[i] + nums[j] + nums[k] == 0 and suitlist not in result:
                        result.append(suitlist)
        return result

f = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print f.threeSum(nums)

'''

class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        result = []
        for i in range(0,len(nums)-2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -=1
        return result
f = Solution()
nums = [-1, 0, 1, 2, -1, -4]
nums = [-12,12,-5,-4,-12,11,9,-11,13,1,12,-1,8,1,-9,-11,-13,-4,10,-9,-6,-11,1,-15,-3,4,0,-15,3,6,-4,7,3,-2,10,-2,-6,4,2,-7,12,-1,7,6,7,6,2,10,-13,-3,8,-12,2,-5,-12,6,6,-5,6,-5,-14,9,9,-4,-8,4,2,-7,-15,-11,-7,12,-4,8,-5,-12,-1,12,5,1,-5,-1,5,12,9,0,3,0,3,-14,2,-4,2,-4,0,1,7,-13,9,-1,13,-12,-11,-6,11,-1,-10,-5,-3,10,3,7,-6,-15,-4,10,1,14,-12]
print f.threeSum(nums)
nums.sort()
print nums
