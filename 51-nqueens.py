class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        def DFS(queens, xy_diff, xy_sum):
            r = len(queens)
            if r == n:
                res.append(queens)
                return
            for c in range(n):
                if c not in queens and r - c not in xy_diff and r + c not in xy_sum:
                    DFS(queens+[c], xy_diff + [r-c], xy_sum + [r+c])
        
        DFS([],[],[])
        return [["." * i + "Q" + "." * (n-i-1) for i in x ] for x in res]

if __name__ == '__main__':
    s = Solution()
    result = s.solveNQueens(5)
    print(len(result))