class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for s in strs:
            cnt = [0 for _ in range(26)]
            
            for ch in s:
                cnt[ord(ch) - ord("a")]+=1
            
            hmap[tuple(cnt)].append(s)
    
        return list(hmap.values())
        