'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作
'''
nums = [1,3,5,8,0,9,0,8]
from typing import List
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         total_zero=0
#         for i in nums:
#             if i==0:
#                 total_zero+=1
#         nums[:] = filter(lambda x: x != 0, nums)
#         print(nums)
#         for j in range(total_zero):
#             nums.append(0)
#         return nums
#
# sol = Solution()
# print(sol.moveZeroes(nums))

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
# 最开始设置两个指针，从头开始读数据
# i是遍历整个数组的指针
# j则是作为0的遍历，j停留的位置就是0所在的位置
        i = 0
        j = 0
        for i in range(len(nums)):#i指针开始遍历整个列表
            if nums[i]!=0:#当i遍历到的数字不为0的时候，那么将它与为0的位置的j进行换位
                nums[i],nums[j]= nums[j],nums[i]
#因为换位结束，那么j的位置就不是0了，所以j要开始找下一个0的位置
                j+=1


#如果i遍历到的数字是0，那么不进行换位，i继续找下一个不是0的数字
        return nums



sol = Solution2()
# print(sol.moveZeroes(nums))
sol.moveZeroes(nums)