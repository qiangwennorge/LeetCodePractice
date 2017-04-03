# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 13:54:47 2017

@author: qiangwennorge
"""
''' 
Given nums = [2,7,11,15], target = 9
because nums[0] + nums[1] = 9
return [0,1]
'''

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    pass

f = Solution()
nums = [2,7,11,15]
target = 9
print f.twoSum(nums, target)