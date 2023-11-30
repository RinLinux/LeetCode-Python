class Solution:
    def totalNQueens(self, n: int) -> int:
        def DFS(r, c, xy_diff, xy_sum):
            if r == n:
                return True
            for col in range(n):
                if col not in c and r + col not in xy_sum and r - col not in xy_diff:
                    if DFS(r+1, c+[col], xy_diff+[r-col], xy_sum+[r+col]):
                        self.res += 1
        self.res = 0
        DFS(0, [], [], [])
        return self.res

if __name__ == '__main__':
    s = Solution()
    result = s.totalNQueens(4)
    print(result)