"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4
   /
  11 

your function should return the depth = 4.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    # Your code here
    # base case(s) 
    # if we have an empty tree, return 0 
    if root is None:
        return 0 
    # how do we get closer to a base case? 
    # we recurse to the left and right 
    left_height = maxDepth(root.left) + 1
    right_height = maxDepth(root.right) + 1 

    return max(left_height, right_height)
