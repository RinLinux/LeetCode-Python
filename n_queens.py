# encoding: utf-8

"""
date: 2020/03/07/13/20

"""


class Solution:
    def solveNQueens(self, n: int):
        if n < 1: return []
        self.cols = set()
        self.left = set()
        self.right = set()
        self.res = []

        self.solver(n, 0, [])
        return self.print_result(n)

    def solver(self, n, row, current_state):

        if row >= n:
            self.res.append(current_state)
            return

        for col_x in range(n):
            if col_x in self.cols or col_x + row in self.left or col_x - row in self.right:
                continue

            self.cols.add(col_x)
            self.left.add(col_x + row)
            self.right.add(col_x - row)

            self.solver(n, row + 1, current_state + [col_x])

            self.cols.remove(col_x)
            self.left.remove(col_x + row)
            self.right.remove(col_x - row)

    def print_result(self, n):
        board = []
        for num in self.res:
            for i in num:
                board.append("."*i + "Q" + "."*(n - i -1))

        table = []
        for j in range(0, len(board), n):
            table.append(board[j:j+n])

        return table



if __name__ == '__main__':
    s = Solution()
    result = s.solveNQueens(4)
    print(result)
