# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 18:58:20 2017

@author: qiangwennorge
"""

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = str(l1.val)
        num2 = str(l2.val)
        
        while l1.next:
            l1 = l1.next
            num1 = str(l1.val) + num1
        while l2.next:
            l2 = l2.next
            num2 = str(l2.val) + num2
            
        num3 = list(str(int(num1) + int(num2)))
    
        n1 = ListNode(int(num3.pop(0)))
        n = n1
        while num3:
            n = ListNode(int(num3.pop(0)))
            n.next = n1
            n1 = n
        return n



