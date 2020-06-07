# encoding: utf-8

"""
date: 2020/03/12/11/54

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        pre_pre_s = 1
        pre_s = 2
        all_s = 0
        for i in range(2, n, 1):
            all_s = pre_pre_s + pre_s
            pre_pre_s = pre_s
            pre_s = all_s

        return all_s

s = Solution()
print(s.climbStairs(4))

