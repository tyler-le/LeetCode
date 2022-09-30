class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # map count -> list
        hmap = collections.defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for ch in word:
                count[ord('a') - ord(ch)]+=1
                
            hmap[tuple(count)].append(word)
            
        return hmap.values()