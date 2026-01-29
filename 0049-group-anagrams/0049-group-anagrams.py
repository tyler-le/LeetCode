class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group by their tuple counts
        hmap = defaultdict(list)

        for word in strs:
            arr = [0 for _ in range(26)]

            for ch in word:
                arr[ord(ch) - ord('a')]+=1
            
            hmap[tuple(arr)].append(word)
        
        return list(hmap.values())


