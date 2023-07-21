class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        occurrences = []
        new_s = ""
        for ch in s:
            if ch.lower() in vowels:
                occurrences.append(ch)
        print(occurrences)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                new_s+=occurrences.pop()
            else:
                new_s+=s[i]
                
        return new_s
        
                        
        
        
        