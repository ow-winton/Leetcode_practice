 ***5/3/2024***
# 第一天更新leetcode做题记录
 今天解决的第一个问题是twoSum
 两种解法

## 暴力枚举
```nums = [2,7,11,15]
target = 9
#方法一 时间复杂度n2 空间复杂度1
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


solution_instance = Solution()
print(solution_instance.twoSum(nums,target)) 
```

## 哈希表查找余数
```commandline
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result ={}
        for i in range(len(nums)):
            print(target-nums[i])
            if target-nums[i] in result:
                return [i,result[target - nums[i]]]
            else:
                result[nums[i]] =i
        print(result)
solution_instance = Solution2()
print(solution_instance.twoSum(nums,target))

```

针对哈希表查余数的话还更新了一版使用enumerate生成索引和值对来进行遍历的方法
```commandline

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for  i,num in enumerate(nums):
            com = target-num
            if com in dict:
                return [i,dict[com]]
            else:
                dict[num]= i
sol = Solution3()
print(sol.twoSum(nums,target))
```
## 需要注意的点
1. 注意的是这个题是让返回索引
2. 其次就是对字典使用in来检索的时候是检索的键，所以哈希存储的时候是
```dict[num]= i```
这样保存的，这样保存可以使得在in的时候通过键检查这个值是否存在，而匹配成功的时候返回对应的索引值