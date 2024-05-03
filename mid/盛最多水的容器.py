'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
'''
a = [1,8,6,2,5,4,8,3,7]
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxL= 0
        left = 0
        right = len(height)-1
        while left<right:
            if height[left]>height[right]:
                maxL = max(maxL,(right-left)*height[right])
                right -= 1
            else:
                maxL= max(maxL,(right-left)*height[left])
                left += 1
        return maxL
sol = Solution()
print(sol.maxArea(a))