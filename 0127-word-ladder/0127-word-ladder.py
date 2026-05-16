class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visited = set()
        wordList = set(wordList)
        q = deque([(beginWord, 1)])
        visited.add(beginWord)

        while q:
            popped_word, popped_dist = q.popleft()
            if popped_word == endWord: return popped_dist

            for i in range(len(popped_word)):
                x = list(popped_word)
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    x[i] = ch
                    new_word = "".join(x)
                    if new_word not in wordList: continue
                    if new_word in visited: continue               
                    q.append((new_word, 1 + popped_dist))
                    visited.add(new_word)

        return 0



        