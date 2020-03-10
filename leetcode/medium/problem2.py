"""
LeetCode | Problem 2: Add Two Numbers

Task:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l2 or l1

    result = ListNode(0)
    pt = result

    while l1 or l2:
        if not l1:
            pt.val += l2.val
            l2 = l2.next
        elif not l2:
            pt.val += l1.val
            l1 = l1.next
        else:
            pt.val += l1.val + l2.val
            l1, l2 = l1.next, l2.next

        if pt.val > 9:
            pt.next = ListNode(1)
            pt.val = pt.val % 10
        elif not l1 and not l2:
            pt.next = None
        else:
            pt.next = ListNode(0)

        pt = pt.next

    return result
