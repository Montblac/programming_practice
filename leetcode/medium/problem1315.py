'''
LeetCode | Problem 1315: Sum of Nodes with Even-Valued Grandparent

Task:
    Given a binary tree, return the sum of values of nodes with even-valued
    grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

    If there are no nodes with an even-valued grandparent, return 0.

Example:
    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 18
    Explanation: The red nodes are the nodes with even-value grandparent while
        the blue nodes are the even-value grandparents.

Constraints:
    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sumEvenGrandparent(root: TreeNode) -> int:
    if not root or (not root.right and not root.left):
        return 0

    def sumChildren(parent):
        if not parent or (not parent.right and not parent.left):
            return 0

        if not parent.right:
            return parent.left.val
        elif not parent.left:
            return parent.right.val
        else:
            return parent.left.val + parent.right.val

    if root.val % 2 == 0:
        return sumChildren(root.left) + \
                sumChildren(root.right) + \
                self.sumEvenGrandparent(root.left) + \
                self.sumEvenGrandparent(root.right)

    return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
