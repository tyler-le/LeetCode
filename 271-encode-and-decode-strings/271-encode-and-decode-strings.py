class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for word in strs:
            encoded += word
            encoded += u'\u00a3' 
            
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        new_word = ""
        for ch in s:
            if ch == u'\u00a3':
                res.append(new_word)
                new_word = ""
            else:
                new_word += ch
                
        return res
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))