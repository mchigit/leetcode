"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.


Solution:

Notice what we are comparing:
1) right.right = left.left
2) right.left = left.right
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isSymmetricRe(root.left, root.right)

    def isSymmetricRe(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None or right.val != left.val:
            return False

        return self.isSymmetricRe(left.left, right.right) and self.isSymmetricRe(left.right, right.left)
