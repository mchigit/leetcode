"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Solution:

Just perform a BFS
"""

# Definition for a binary tree node.
from queue import Queue

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        output = []
        q = Queue()
        q.put(root)
        while not q.empty():
            current_level = []
            for _ in range(q.qsize()):
                curr = q.get()
                current_level.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)

            output.append(current_level)

        return output
 

