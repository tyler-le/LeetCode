class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map character count : list of words
        hmap = defaultdict(list)
        
        for s in strs:
            freq = [0]*26
            for ch in s:
                freq[ord(ch) - ord('a')]+=1
                
            hmap[tuple(freq)].append(s)
        
        return hmap.values()
            