# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:21:21 2017

@author: qiangwennorge
"""

'''
 Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]

'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.dfsfunc(candidates, target, 0, [], result)
        return result
        
    def dfsfunc(self, nums, target, index, path, result):
        if target < 0:
            return result
        elif target == 0:
            result.append(path)
            return result
        for i in xrange(index, len(nums)):
            self.dfsfunc(nums, target - nums[i], i, path + [nums[i]], result)
            print path, path + [nums[i]]
        
f = Solution()
print f.combinationSum([2,3,6,7],7)

        