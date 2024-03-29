"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Solution:

Traverse through the tree, also pass down the minimum and maximum value that the root cannot violate
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        return self.isValid(root.left, -float("inf"), root.val) and self.isValid(root.right, root.val, float("inf"))

    def isValid(self, root, minV, maxV) -> bool:
        if not root:
            return True

        if root.val <= minV or root.val >= maxV:
            return False

        return self.isValid(root.left, minV, root.val) and self.isValid(root.right, root.val, maxV)
