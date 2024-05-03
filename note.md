 ***5/3/2024 day1***
# leetcode做题记录

# 最长连续序列
```commandline

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

```
## 总结
这个题其实也很简单，理解难度也不高
1. 总结来说意思就是先判断这个数字可不可能是最长连续序列的起始值，这个通过判断这个数字-1是否存在在序列中来判断
2. 如果它是起始值才进行后续，不是就跳到下一个数字
3. 如果是起始值，那么用while循环累加判断这个数+1是否存在于序列里面，然后循环判断这一轮的序列长度是多少
4. 判断清楚序列长度以后与当前最长序列的长度进行对比取大，最终返回最大值
## 注意的点
1. 注意序列可能有重复值，用```set()```方法进行一次去重。
# 字母异位词 
## 哈希解法
```commandline
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for st in strs:
            key = "".join(sorted(st))
            if key not in dict:
                dict[key]=[]
            dict[key].append(st)
        return list(dict.values())

s = Solution()
print(s.groupAnagrams(strs))
```
## 注意的点
1. 通过对所有单词sort能检查单词是否相同
2. 对比后相同的单词有着同样的标志词***key***
3. 在哈希表中同一个key对应着多个异位词语，他们用列表存放到key对应的value中
4. 需要注意，在存放key时候，要判断key不在dict里的时候要进行初始化，否则无法直接皴法。在存放到列表的时候，要对存放的单词的列表进行初始化

# twoSum
 两种解法

## 暴力枚举
```
nums = [2,7,11,15]
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