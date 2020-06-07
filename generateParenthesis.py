# encoding: utf-8

"""
date: 2020/03/05/17/35

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            return

        if left < n:
            self._gen(left + 1, right, n, result + "(")
        if right < n and left > right:
            self._gen(left, right + 1, n, result + ")")


if __name__ == '__main__':
    s = Solution()
    ss = s.generateParenthesis(10)
    print(ss)