class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        
        for c in s:
            d1[c]+=1
        for c in t:
            d2[c]+=1
        
        return d1 == d2