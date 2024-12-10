class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransom note should be a subset of magazine
        
        ransom_ctr = Counter(ransomNote)
        magazine_ctr = Counter(magazine)
        
        # assert that the counts for each char in ransom is less than or equal to magazine
        for ch in ransomNote:
            if ransom_ctr[ch] > magazine_ctr[ch]:
                return False
        
        return True