import typing
from typing import List
# 数组遍历，经典线性结构
class shuzu:
    def traverse(arr:List[int]):
        for i in range(len(arr)):
            print(i)
# arr=[1,2,3,4,5,6]
# traverse(arr)

#链表遍历
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
# 创建链表节点
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 构建链表关系
node1.next = node2
node2.next = node3

# 遍历链表

# node1.traverse_recursive()

#二叉树
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

node1 = treenode(1)
node2 = treenode(2)
node3 = treenode(3)
node4 = treenode(4)
node5 = treenode(5)
node6 = treenode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node1.traverse()

