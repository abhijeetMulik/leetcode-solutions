class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)]) # word, steps
        seen = {beginWord}
        wordList = set(wordList)

        while queue:
            start, steps = queue.popleft()
            if start == endWord:
                return steps
            
            for i in range(len(start)):
                for j in range(ord('a'), ord('z') + 1):
                    word = start[:i] + chr(j) + start[i + 1:]
                    if word not in seen and word in wordList:
                        seen.add(word)
                        queue.append((word, steps + 1))
            
        return 0
