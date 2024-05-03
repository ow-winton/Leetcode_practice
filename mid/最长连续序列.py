'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''

nums = [100,4,200,1,3,2]
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_se = 0
        for i in nums_set:
            if i-1 not in nums_set:
                current_num = i
                len_se = 1
            while current_num+1 in nums_set:
                current_num+=1
                len_se+=1
            longest_se = max(longest_se,len_se)

        return longest_se


sol = Solution()
print(sol.longestConsecutive(nums))

