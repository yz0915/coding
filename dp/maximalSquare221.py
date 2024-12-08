# lc 221
# https://leetcode.com/problems/maximal-square/

# Input: matrix = 1 0 1 0 0
#                 1 0 1 0 0
#                 1 1 1 1 1
#                 1 0 0 1 0
# Output: 4

# recursive: top down
# Define the state: dp stores the maximum side length of a square whose top-left corner is at cell (r, c).
def maximalSquare(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    cache = {}  # map each (r, c) -> maxLength of square

    def helper(r, c):
        # BASE CASE!!
        if r >= ROWS or c >= COLS:
            return 0

        if (r, c) not in cache:
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            diag = helper(r + 1, c + 1)

            cache[(r, c)] = 0
            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, diag)
        return cache[(r, c)]

    helper(0, 0)
    return max(cache.values()) ** 2