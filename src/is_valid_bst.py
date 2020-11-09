"""
You are given a binary tree. You need to write a function that can determine if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- No duplicates in the binary tree. 
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.

Example 3:

    10
   /  \
  2   18
      / \
     6  21

Output: False

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# is this function expecting an answer? 
def is_valid_BST(root):
    # Your code here
    # keep track of the valid range as we're traversing down the tree 
    # when we go left, limit the upper bound to be root - 1 
    # when we go right, limit the lower bound to be root + 1 
    # check if the current node's value falls within the range
    # check the root's left child
        # if the left's child value >= root's value 
            # return False
    # check the root's right child 
        # if the right's child value <= root's value 
            # return False 
    # otherwise, return True 
    return recurse(root, float('-inf'), float('inf'))

def recurse(root, min_bound, max_bound):
    # base case(s) 
    # check the current value against the range 
    # we've traversed the whole tree and never saw a False, so return True 
    if root is None:
        return True
    # if the current value falls outside the range, return False 
    if root.value < min_bound or root.value > max_bound:
        return False 
    # how do we get closer to our base case? 
    # recurse with the left child and update the range 
    left = recurse(root.left, min_bound, root.value - 1)
    # recurse with the right child and update the range 
    right = recurse(root.right, root.value + 1, max_bound)

    # if either left or right is False, return False 
    return left and right 

