class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for word in strs:
            encoded += word
            encoded += '\0'
            
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        new_word = ""
        for ch in s:
            if ch == '\0':
                res.append(new_word)
                new_word = ""
            else:
                new_word += ch
                
        return res