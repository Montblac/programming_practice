"""
LeetCode | Problem 14: Longest Common Prefix

Task:
    Write a function to find the longest common prefix string amongst an array
    of strings. If there is no common prefix, return an empty string "".

Examples:
    Example 1:
        Input: ["flower","flow","flight"]
        Output: "fl"

    Example 2:
        Input: ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.

Note:
    All given inputs are in lowercase letters a-z.
"""


def longestCommonPrefix(strs: [str]) -> str:
    if not strs:
        return ""

    strs_size = len(strs)
    word = min(strs, key=len)

    # Solution 1
    for i in range(len(word), 0, -1):
        prefix = word[:i]
        for count, s in enumerate(strs, 1):
            if not s.startswith(prefix):
                break
            if count == strs_size:
                return prefix

    # Solution 2: Faster, but more space used
    '''
    prefixes = [word[:i] for i in range(len(word), 0, -1)]
    for prefix in prefixes:
        for count, s in enumerate(strs, 1):
            if not s.startswith(prefix):
                break
            if count == strs_size:
                return prefix
    '''

    return ''


if __name__ == '__main__':

    input1 = ['flower', 'flow', 'flight']
    assert longestCommonPrefix(input1) == 'fl'

    input2 = ['dog', 'racecar', 'car']
    assert longestCommonPrefix(input2) == ''

    input3 = ['ca', 'a']
    assert longestCommonPrefix(input3) == ''

    input4 = []
    assert longestCommonPrefix(input4) == ''

    input5 = ['a']
    assert longestCommonPrefix(input5) == 'a'
