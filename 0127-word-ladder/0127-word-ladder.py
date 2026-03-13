class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        visited = set()

        q = deque([(beginWord, 1)])

        while q:
            popped_word, popped_dist = q.popleft()

            if popped_word == endWord:
                return popped_dist

            for i in range(len(popped_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = popped_word[:i] + ch + popped_word[i+1:]
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, popped_dist + 1))
        
        return 0
            
