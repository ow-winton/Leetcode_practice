from typing import List
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        root = inorder.index(preorder[2])
        return root





sol =Solution()
print(sol.buildTree(preorder,inorder))