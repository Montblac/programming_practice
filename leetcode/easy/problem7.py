"""
LeetCode | Problem 7: Reverse Integer

Task:
    Given a 32-bit signed integer, reverse digits of an integer.

Example:
    Input: 123
    Output: 321

    Input: -123
    Output: -321

    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        value = int(str(abs(x))[::-1])
        result = sign * value
        if (-1 << 31) <= result <= (1 << 31) - 1:
            return result
        return 0
