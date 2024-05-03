 ***5/3/2024 day1***
# leetcode做题记录

# 移动零

## 错误解
最开始我使用的是切片赋值和lambda推导式来生成列表，但是很遗憾切片赋值其实也是一种复制，本体要求不可以复制，所以切片赋值是错误解，但是记录一下
```commandline

nums = [0,1,0,3,12]
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total_zero=0
        for i in nums:
            if i==0:
                total_zero+=1
        nums[:] = filter(lambda x:x!=0,nums)
        print(nums)
        for j in range(total_zero):
            nums.append(0)
        return nums

sol = Solution()
print(sol.moveZeroes(nums))
```
这串代码我唯一需要记一下的是lambda表达式的写法，毕竟不太常用

还有一个小点注意一下就是filter，他是可以接受一个函数还有一个可迭代对象来作为输入的
```commandline
nums[:]= filter(lambda x: x!=0,nums)
```
## 正确解
```commandline
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

```
## 总结
这个算法稍微有点难以理解，最开始我非常不理解为什么j永远指向0，但实际上我是被给的例子误解了，把例子换成``` nums = [1,3,5,8,0,9,0,8]```我们就能清楚的理解了，如果列表完全没有0，其实i和j两个指针就是单纯的一前一后的遍历整个列表，但是如果列表有0的话，i会跳过一次循环，导致j在上一轮+1后本轮停留的位置就是i跳过的0的位置，j会停留在这里，于是i找到下一个非0元素的时候会跟这个j指向的0交换位置

这也就是为什么j这个指针总是神奇的指向0，这并不神奇，他只是单纯的遍历整个列表找到了这个0的位置而已

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