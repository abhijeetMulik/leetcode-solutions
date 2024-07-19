class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, 1)]) #start, steps
        seen ={beginWord}
        wordList = set(wordList)

        while q:
            start, steps = q.popleft()
            if start == endWord:
                return steps

            for i in range(len(start)):
                for j in range(ord('a'), ord('z') + 1):
                    trans = start[:i] + chr(j) + start[i + 1:]
                    # print(trans)
                    if trans not in seen and trans in wordList:
                        seen.add(trans)
                        q.append((trans, steps + 1))
        return 0
        