"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:
Input: n = 1
Output: [["Q"]]
Constraints:
1 <= n <= 9
"""
from typing import List


class Solution:
    def __init__(self):
        self.solutions = []
        self.n = None

    # Function to check if two queens threaten each other or not
    def isSafe(self, mat, r, c):

        # return false if two queens share the same column
        for i in range(r):
            if mat[i][c] == 'Q':
                return False

        # return false if two queens share the same `\` diagonal
        (i, j) = (r, c)
        while i >= 0 and j >= 0:
            if mat[i][j] == 'Q':
                return False
            i = i - 1
            j = j - 1

        # return false if two queens share the same `/` diagonal
        (i, j) = (r, c)
        while i >= 0 and j < self.n:
            if mat[i][j] == 'Q':
                return False
            i = i - 1
            j = j + 1
        return True

    def helper(self, mat, r):
        # if `N` queens are placed successfully, print the solution
        if r == self.n:
            self.solutions.append(["".join(el) for el in mat])
            return
        # place queen at every square in the current row `r`
        # and recur for each valid movement
        for i in range(self.n):
            # if no two queens threaten each other
            if self.isSafe(mat, r, i):
                # place queen on the current square
                mat[r][i] = 'Q'
                # recur for the next row
                self.helper(mat, r + 1)
                # backtrack and remove the queen from the current square
                mat[r][i] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.helper(board, 0)
        return self.solutions


if __name__ == '__main__':
    s = Solution()
    # print(s.solveNQueens(1))
    # print(s.solveNQueens(2))
    # print(s.solveNQueens(3))
    # print(s.solveNQueens(4))
    # print(s.solveNQueens(5))
    # print(s.solveNQueens(6))
    # print(s.solveNQueens(7))
    # print(s.solveNQueens(8))
    # print(s.solveNQueens(9))
