class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
        
        for key, value in ransom.items():
            if key not in mag: return False
            elif mag[key] < value: return False
        return True