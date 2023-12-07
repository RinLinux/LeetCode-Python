import collections


class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        dic = collections.defaultdict(list)
        n = len(wordList[0])
        for w in words:
            for i in range(n):
                dic[w[:i] + '*' + w[i + 1:]].append(w)
        q, s = [(beginWord, [beginWord])], []
        res = []
        seen = set()
        while q:
            while q:
                w, path = q.pop()
                seen.add(w)
                if w == endWord:
                    res.append(path)
                for i in range(n):
                    for nxt in dic[w[:i] + '*' + w[i + 1:]]:
                        if nxt not in seen:
                            s.append((nxt, path + [nxt]))
            if res:
                return res
            q, s = s, q
        return []


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    s = Solution()
    res = s.findLadders(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(res)
