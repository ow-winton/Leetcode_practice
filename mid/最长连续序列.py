'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''

nums = [100,4,200,1,3,2]
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict={}
        sorted(nums)
