class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # group the anagrams using a hashmap and return a list of all the values
        # [character counts] : [list of words]
        
        hmap = collections.defaultdict(list)
        ret = []
        
        for s in strs:
            counts = [0]*26
            for ch in s:
                counts[ord(ch) - ord('a')]+=1
            hmap[tuple(counts)].append(s)
        
        for group in hmap.values():
            ret.append(group)
        
        return ret