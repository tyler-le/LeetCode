class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        hmap, p_map = collections.defaultdict(int), Counter(p)
        l, window_size, res = 0, len(p), []
        
        for r in range(len(s)):
            hmap[s[r]]+=1
            
            if r-l+1 > window_size:
                hmap[s[l]]-=1
                if not hmap[s[l]]: del hmap[s[l]]
                l+=1
            
            if hmap == p_map: 
                res.append(l)
                
        return res
            
            
                