class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group by their tuple counts
        hmap = defaultdict(list)

        for word in strs:
            cnt = Counter(word)
            arr = [0 for _ in range(26)]

            for ch, freq in cnt.items():
                arr[ord(ch) - ord('a')]+=freq
            
            hmap[tuple(arr)].append(word)
        
        return list(hmap.values())


