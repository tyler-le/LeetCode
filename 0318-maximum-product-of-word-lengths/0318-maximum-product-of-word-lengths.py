class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        res = 0

        char_set = {}
        for word in words:
            char_set[word] = set(word)

        for i in range(n):
            for j in range(i+1, n):

                bits_a = [0 for _ in range(26)] 
                bits_b = [0 for _ in range(26)]

                letters_a = char_set[words[i]]
                letters_b = char_set[words[j]]
                
                bitwise_and = letters_a & letters_b

                if not len(letters_a & letters_b):
                    res = max(res, len(words[i]) * len(words[j]))

        return res