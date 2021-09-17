# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        if root1.val == root2.val:
            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        return self.isMirror(root.left, root.right)
