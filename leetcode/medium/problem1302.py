'''
LeetCode | Problem 1302: Deepest Leaves Sum

Task:
    Given a binary tree, return the sum of values of its deepest leaves.

Example:
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15


Constraints:
    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def deepestLeavesSum(self, root: TreeNode) -> int:
    def getMaxDepth(root, depth):
        if not root:
            return depth - 1
        return max(getMaxDepth(root.left, depth + 1), getMaxDepth(root.right, depth + 1))

    def getTotal(root, depth):
        if not root:
            return 0
        if depth == max_depth:
            return root.val
        return getTotal(root.left, depth + 1) + getTotal(root.right, depth + 1)

    max_depth = getMaxDepth(root, 0)
    total = getTotal(root, 0)
    return total
