# 目录

# labuladong 代码整理
- [chapter2](#第二章)
# 简单题目
- [移动零](#移动零)
- [twosum](#twosum)

# 中等题目
- [最长连续序列](##最长连续序列)
- [字母异位词 ](#字母异位词 )
- [最多水的容器](#最多水的容器)
- [三数之和](#三数之和)
***5/4/2024 day2***
# labuladong 学习之路
# 第二章
1. 首先这里编写的是最简单的python数组遍历结构，这个结构是一个线性结构，并不难理解
```commandline
def traverse(arr:List[int]):
    for i in range(len(arr)):
        print(i)
arr=[1,2,3,4,5,6]
traverse(arr)
```

2. 链表遍历的python写法 两种：1. 线性 2.非线性递归
```commandline
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(head):
        p = head
        while p is not None:
            print(p.val)  # 做一些操作，这里简单打印节点的值
            p = p.next

    def traverse_recursive(head) -> None:
        def traverse(head):
            if head is None:
                return
            print(head.val)  # 这里进行相应的操作，这里简单打印节点的值
            traverse(head.next)
        traverse(head)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 构建链表关系
node1.next = node2
node2.next = node3

# 遍历链表

node1.traverse_recursive()
```
3. 树型结构的遍历
#### 注意的点
1. python无法异构函数，所以要定义多个函数
2. 递归调用函数最外层无法递归，因为会报错没有定义，所以要在函数内部定义嵌套函数，用嵌套函数实现递归
针对这个的原因
```
为什么内部函数可以递归调用呢？这是因为当你调用一个函数时，Python 解释器会在当前作用域中查找该函数的定义。如果在当前作用域中找不到该函数的定义，解释器会向上一级作用域继续查找，直到找到为止。而内部函数是定义在外部函数的作用域内的，因此当内部函数调用自身时，解释器会在外部函数的作用域中找到函数定义，从而可以成功地进行递归调用。

相反，如果你在外部函数内部调用外部函数自身，那么解释器会在当前作用域中找不到函数定义，因为函数的定义不在当前作用域内，从而导致找不到函数定义的错误
```
```commandline
class treenode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(root):

        def tra(root):
            if root is None:
                return
            print(root.val)
            tra(root.left)
            tra(root.right)
        tra(root)


```
***5/3/2024 day1***（6道题）
# leetcode做题记录

# 三数之和
## 难点
1. 难点在于去除重复解，如我提供的错误超时解，它在最后才开始去除错误解，导致超时
2. 为此需要在算法进行中就把重复解去除，其实也很简单，判断一下当前项和下一项一不一样就行了
3. 对于提供的性能较差的解需要注意的点是对i的限制条件是```if i>0 and nums[i]==nums[i-1]:```,如果不这样限制，而是```if nums[i]==nums[i+1] ```这样的情况会缺少解，所以这告诉我们去重的时候要考虑到先执行一次，然后第二次的时候判断前面出没出现过，而不是还没执行判断后续会重复就直接跳过，这会导致返回的结果缺少解

## 性能稍好的解
这个比刚刚提高了一点性能，但不多，我也不知道什么是高性能算法了，就这样把
```commandline
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

```
## 性能较差的解
这个解释能正常通过测试，但是性能太差
```commandline
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

```

## 超时的错误解（能输出正确结果，但是超时）
```commandline
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#首先排序
        nums = sorted(nums)
        l = len(nums)
        result = []

        for i in range(l-2):
            j = i + 1
            k = l - 1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum ==0:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k -= 1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k -= 1
        final_result = []
        for i in result:
            if i not in final_result:
                final_result.append(i)
        return final_result
sol = Solution()
print(sol.threeSum(nums))

```
# 最多水的容器
## 两指针
```commandline
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

```

## 注意点
1. 注意计算完面积再迭代，否则会出错
## 暴力迭代（能出解，但是会超时）
```commandline
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxL= 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i!=j:
                    k = min(height[i],height[j])
                    l = k*abs(i-j)
                    maxL = max(maxL,l)
        return maxL



```
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

## 注意点
本题的要求是不能复制列表

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