# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isDoubleSame(m: TreeNode, n: TreeNode) -> bool:
            if not m and not n:
                return True
            elif not m or not n:
                return False
            if m.val != n.val:
                return False
            return isDoubleSame(m.left, n.right) and isDoubleSame(m.right, n.left)

        return isDoubleSame(root, root)
