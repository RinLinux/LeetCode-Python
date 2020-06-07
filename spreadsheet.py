# encoding: utf-8

"""
date: 2020/03/08/23/48

"""

def coverSheetCode(s):
    num = 0
    count = len(s)
    for i in s:
        num += 26**(count-1) * (ord(i) - ord("A") + 1)
        count -= 1
    return num

if __name__ == '__main__':
    print(coverSheetCode("AZ"))
