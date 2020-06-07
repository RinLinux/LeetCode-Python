# encoding: utf-8

"""
date: 2020/03/08/17/39

"""

class lookAndSay():

    def next_num(self,s):
        res = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            res.append(str(count) + s[i])
            i += 1
        return ''.join(res)

    def get_nth(self,n):
        s = '1'
        for i in range(n):
            s = self.next_num(s)
        return s


if __name__ == '__main__':
    seq = lookAndSay()
    print(seq.get_nth(3))