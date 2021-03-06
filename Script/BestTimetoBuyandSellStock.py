# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 09:21:39 2017

@author: qiangwennorge
"""

'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        elif len(prices) == 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(0,len(prices)):
            print min_price, prices[i]
            
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            print max_profit
        return max_profit
        
            
            
f = Solution()
inputprice = [7, 1, 5, 3, 6, 4]
print f.maxProfit(inputprice)           
