# encoding: utf-8

"""
date: 2020/03/09/16/19

"""
s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    i = 0
    j = len(s) - 1

    while(i < j):
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

print(isPalindrome(s))

class Solution:
    def delNodes(self, root, to_delete):
        ans = []
        ds = set(to_delete)
        ans = self.process(root, ans, ds)
        return ans

    def process(self, n, ans, ds):
        if not n: return None
        n.left, n.right = self.process(n.left), self.process(n.right)
        if n.val not in ds: return n
        if n.left: ans.append(n.left)
        if n.right: ans.append(n.right)
        if n: ans.append(n)
        return None
