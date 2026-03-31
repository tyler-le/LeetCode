class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        n = len(words)
        
        ranks = {}
        ranks[""] = 0
        for i in range(len(order)):
            ranks[order[i]] = i + 1


        for i in range(n-1):
            prev, after = words[i], words[i+1]

            p1, p2 = 0, 0

            while p1 < len(prev) and p2 < len(after) and prev[p1] == after[p2]:
                p1+=1
                p2+=1

            # print(f"{prev} and {after} first differ at p1={p1}, p2={p2}")
            rank1 = ranks[prev[p1]] if p1 < len(prev) else 0
            rank2 = ranks[after[p2]] if p2 < len(after) else 0
            if rank1 > rank2: 
                return False

        return True