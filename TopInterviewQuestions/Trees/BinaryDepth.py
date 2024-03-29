"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Solution:

Leverage recursion
Depth at each level is the maximum of the level of its children
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        rightDepth = self.maxDepth(root.right) + 1
        leftDepth = self.maxDepth(root.left) + 1

        return max(leftDepth, rightDepth)

