'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词

'''
from typing import List
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

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