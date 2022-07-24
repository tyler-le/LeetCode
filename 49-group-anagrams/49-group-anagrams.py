class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        
        # map (char count) -> list
        for s in strs:
            char_count = [0 for i in range(26)]
            for ch in s: char_count[ord(ch) - ord('a')] += 1
            res[tuple(char_count)].append(s)
            
        return list(res.values())
            