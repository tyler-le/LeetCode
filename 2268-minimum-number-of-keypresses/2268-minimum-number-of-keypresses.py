class Solution:
    def minimumKeypresses(self, s: str) -> int:
        chars = set(s)
        freqs = Counter(s)
        indices = defaultdict(int)

        hmap = defaultdict(list)

        arr = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

        index = 0

        for ch, freq in arr:
            hmap[index].append(ch)
            indices[ch] = len(hmap[index]) - 1
            index = (index + 1) % 9

        print(indices)
        res = 0
        for ch, index in indices.items():
            res+=(freqs[ch] * (index + 1))

        return res




