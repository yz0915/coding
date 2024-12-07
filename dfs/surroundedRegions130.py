# lc 130
# https://leetcode.com/problems/surrounded-regions/

# Example 1:

# Input: X X X X
#        X O O X
#        X X O X
#        X O X X

# Output:X X X X
#        X X X X
#        X X X X
#        X O X X


def solve(board):
    rows, cols = len(board), len(board[0])
    flag = set()

    def dfs(r, c):
        # BASE CASE!!! defines the conditions under which the recursion should stop
        if not(r in range(rows) and c in range(cols)) or board[r][c] != 'O' or (r, c) in flag:
            return
        flag.add((r, c))
        return (dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))

    # traverse through the board
    for r in range(rows):
        for c in range(cols):
            if( (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == 'O'):
                dfs(r, c)

    # set all of the 'X's to 'O's
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r, c) not in flag:
                board[r][c] = 'X'