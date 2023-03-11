class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        res = []
        
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord("a") - ord(ch)]+=1
            hmap[tuple(count)].append(s)
        
        return hmap.values()
            
