# encoding: utf-8

"""
date: 2020/03/06/21/11

"""
class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.val = self.PossibleVals()
        # print(self.val)
        self.Solver()
        return board


    def PossibleVals(self):
        val = {}
        numbers = {str(i) for i in range(1, 10)}
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    res = set()
                    a = (i // 3) * 3
                    b = (j // 3) * 3

                    for u in range(9):
                        res.add(self.board[u][j])
                        res.add(self.board[i][u])
                        res.add(self.board[u // 3 + a][u % 3 + b])
                    res.remove('.')
                    val[(i, j)] = numbers - res
        return val


    def Solver(self):
        if len(self.val) == 0:
            return True
        pss = self.val
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update = {kee: self.val[kee]}
            if self.ValidOne(n, kee, update):  # valid choice
                if self.Solver():  # keep solving
                    return True
            self.undo(kee, update)  # invalid choice or didn't solve it => undo
        return False


    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        xx = kee[0]
        yy = kee[1]
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0] == i or ind[1] == j or (ind[0] / 3, ind[1] / 3) == (i / 3, j / 3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind]) == 0:
                        return False
        return True


    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = "."
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].add(update[k])


if __name__ == '__main__':
    m = [
        ['6', '.', '.', '1', '.', '.', '7', '.', '8'],
        ['.', '.', '.', '8', '.', '.', '2', '.', '.'],
        ['2', '3', '8', '.', '5', '.', '1', '.', '.'],
        ['.', '.', '.', '.', '4', '.', '.', '9', '2'],
        ['.', '.', '4', '3', '.', '8', '6', '.', '.'],
        ['3', '7', '.', '.', '1', '.', '.', '.', '.'],
        ['.', '.', '3', '.', '7', '.', '5', '2', '6'],
        ['.', '.', '2', '.', '.', '4', '.', '.', '.'],
        ['9', '.', '7', '.', '.', '6', '.', '.', '4']
        ]
    S = Solution()
    print(S.solveSudoku(m))