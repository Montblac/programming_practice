'''
LeetCode | Problem 654: Maximum Binary Tree

Task:
    Given an integer array with no duplicates. A maximum tree building on this
    array is defined as follow:

    1. The root is the maximum number in the array.
    2. The left subtree is the maximum tree constructed from left part subarray
        divided by the maximum number.
    3. The right subtree is the maximum tree constructed from right part
        subarray divided by the maximum number.

    Construct the maximum tree by the given array and output the root node of
    this tree.

Example 1:
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the following tree:

          6
        /   \
       3     5
        \    /
         2  0
           \
            1
Note:
The size of the given array will be in the range [1,1000].
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 1:
            return None or TreeNode(nums[0])

        node = TreeNode(max(nums))
        idx = nums.index(node.val)
        ltree, rtree = nums[:idx], nums[idx+1:]

        if ltree:
            node.left = self.constructMaximumBinaryTree(ltree)
        if rtree:
            node.right = self.constructMaximumBinaryTree(rtree)

        return node
