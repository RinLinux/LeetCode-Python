# encoding: utf-8

"""
date: 2020/03/12/12/42

"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <=2: return 1
        T0, T1, T2 = 0, 1, 1
        T = 0

        for i in range(2, n):
            T = T0 + T1 + T2
            T0, T1, T2 = T1, T2, T
        return T

S = Solution()
print(S.tribonacci(25))


def fib(n):
    if n <=1: return n
    cache0 = 0
    cache1 = 1
    cache = 0
    for i in range(1, n):
        cache = cache0 + cache1
        cache0 = cache1
        cache1 = cache

    return cache

# if __name__ == '__main__':
#     print(fib(0))
