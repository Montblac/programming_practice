"""
LeetCode | Problem 21: Merge Two Sorted Lists

Task:
    Merge two sorted linked lists and return it as a new list. The new list
    should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Solution 1: Faster, less space usage
    if not l1 or not l2:
        return l1 or l2

    result = None
    if l1.val <= l2.val:
        result = l1
        l1 = l1.next
    else:
        result = l2
        l2 = l2.next
    pt = result

    while l2:
        if not l1 or l2.val < l1.val:
            pt.next = l2
            pt = l2
            l2 = l2.next
        else:
            pt.next = l1
            pt = l1
            l1 = l1.next

    while l1:
        pt.next = l1
        pt = l1
        l1 = l1.next

    # Solution 2
    '''
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
    '''

    return result
