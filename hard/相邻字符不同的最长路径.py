from typing import List

parent  = [-1,0,0,1,1,2]
s = "abacbe"
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        l = len(parent)
        g = [[] for _ in range(l)]
        for i in range(1, l):
            g[parent[i]].append(i)
        res = 0

        def dfs(root):
            zhiqianzuichang = 0
            for child in g[root]:
                dangqianchangdu = dfs(child)+1
                nonlocal res
                if s[child]!= s[root]:
                    res= max(res,zhiqianzuichang+dangqianchangdu)
                    zhiqianzuichang = max(zhiqianzuichang,dangqianchangdu)
            return zhiqianzuichang

        dfs(0)
        return res+1

sol = Solution()
print(sol.longestPath(parent,s))
# l = len(parent)
# g = [[] for _ in range(l)]
# print(g)
# for i in range(1,l):
#     g[parent[i]].append(i)
# print(g)