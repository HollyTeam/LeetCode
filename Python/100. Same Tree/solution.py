# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归调用的时候，p和q为两棵树上对应位置的节点
        if p is None and q is None:  # 两个节点都为空，返回True
            return True
        if (p is not None and q is None) or (p is None and q is not None):  # 一个为空，另一个不为空，返回False
            return False
        if p.val != q.val:  # 两个节点都不为空，但是节点的值不相同，返回False
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
