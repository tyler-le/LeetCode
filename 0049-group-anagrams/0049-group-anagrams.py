class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        res = []
        
        for word in strs:
            count = [0]*26
            
            for ch in word:
                count[ord(ch) - ord('a')]+=1
            hmap[tuple(count)].append(word)
            
        
        res = hmap.values()
        return res