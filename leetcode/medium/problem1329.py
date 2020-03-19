'''
LeetCode | Problem 1329: Sort the Matrix Diagonally

Task:
    Given a m * n matrix mat of integers, sort it diagonally in ascending order
    from the top-left to the bottom-right then return the sorted array.

Example 1:
    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    1 <= mat[i][j] <= 100
'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        # Create a dictionary with (key, value) as (i-j, [])
        struct = {n:[] for n in range(row - 1, -col, -1)}

        # Store matrix values in structure
        for i in range(row):
            for j in range(col):
                struct[i-j].append(mat[i][j])

        # Sort list of numbers
        for key in struct.keys():
            struct[key].sort()

        # Update matrix
        for i in range(row):
            for j in range(col):
                mat[i][j] = struct[i-j].pop(0)

        return mat
