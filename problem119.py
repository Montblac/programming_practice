"""
LeetCode
Problem 119: Pascal's Triangle II

Task:
    Given a non-negative index k where k ≤ 33, return the kth index row of the
    Pascal's triangle. Note that the row index starts from 0.

Example:
    Input: 3
    Output: [1,3,3,1]

Follow up:
    Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """ Solution 1
        """
        if rowIndex <= 0:
            return [1]

        result = [1]
        for row_num in range(1, rowIndex + 1):
            result.append(1)

            for col in range(row_num-1, 0, -1):
                result[col] = result[col] + result[col-1]
        return result

    def getRow_B(self, rowIndex: int) -> List[int]:
        """ Solution 2
        """
        if rowIndex <= 0:
            return [1]

        row = [1]
        result = []
        for row_num in range(1, rowIndex + 1):
            updated_row = [None] * (row_num + 1)
            updated_row[0], updated_row[-1] = (1, 1)

            for col in range(1, row_num):
                updated_row[col] = row[col-1] + row[col]
            row = updated_row

            if row_num == rowIndex:
                result = row
        return result
