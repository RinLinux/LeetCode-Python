# encoding: utf-8

"""
date: 2020/03/09/16/20

"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1):
            s = s.replace(str(i) + '#'* (i>9), chr(96+i))
        return s



if __name__ == '__main__':
    s = "10#11#12"
    res = Solution()
    print(res.freqAlphabets(s))