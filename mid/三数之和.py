'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''
from typing import List
nums = [-1,0,1,2,-1,-4]
nums = [-4,-1,-1,0,1,2]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#首先排序
        nums = sorted(nums)
        l = len(nums)
        result = []

        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i + 1
            k = l - 1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum ==0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] ==nums[j+1]:
                        j+=1
                    while j<k and nums[k] ==nums[k-1]:
                        k-=1
                    j+=1
                    k -= 1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k -= 1

        return result
sol = Solution()
print(sol.threeSum(nums))


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#首先排序
        nums = sorted(nums)
        l = len(nums)
        result = []
        k =0
        for k in range(l-2):
            if nums[k]>0:
                break
            if k>0 and nums[k]==nums[k-1]:
                continue
            i = k+1
            j = l-1
            while i <j:
                s = nums[i]+nums[j]+nums[k]
                if s <0:
                    i+=1
                    while i<j and nums[i]==nums[i-1]:i+=1
                elif s>0:
                    j-=1
                    while i<j and nums[j]==nums[j+1]:j-=1
                else:
                    result.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return result
sol = Solution1()
print(sol.threeSum(nums))