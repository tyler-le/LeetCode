class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        hmap = collections.defaultdict(int)
        
        for ch in s:
            hmap[ch]+=1
            
            if hmap["R"] == hmap["L"]:
                res+=1
                hmap["R"], hmap["L"] = 0, 0
                
        return res