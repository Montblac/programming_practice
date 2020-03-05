"""
LeetCode | Problem 20: Valid Parentheses

Task:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.
Examples:
    Example 1:
        Input: "()"
        Output: true

    Example 2:
        Input: "()[]{}"
        Output: true

    Example 3:
        Input: "(]"
        Output: false

    Example 4:
        Input: "([)]"
        Output: false

    Example 5:
        Input: "{[]}"
        Output: true
"""
def isValid(s: str) -> bool:
        if len(s) % 2:
            return False

        # Solution 1: Faster & less space
        stack = []
        for c in s:
            if c in '[{(':
                stack.append(c)
            elif not stack:
                return False
            else:
                val = ord(c) - ord(stack.pop())
                if val not in (1,2):
                    return False

        # Solution 2
        '''
        table = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for i in s:
            if i in table:
                stack.append(i)
            elif not stack:
                return False
            else:
                val = stack.pop()
                if i != table[val]:
                    return False
        '''
        return not stack


if __name__ == '__main__':
    test1 = '()'
    assert isValid(test1)

    test2 = '()[]{}'
    assert isValid(test2)

    test3 = "(]"
    assert not isValid(test3)

    test4 = "([)]"
    assert not isValid(test4)

    test5 = "{[]}"
    assert isValid(test5)
