class Codec:

    def __init__(self):
        self.short_to_long = {}
        self.count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = str(self.count)
        self.short_to_long[short_url] = longUrl
        self.count+=1
        return short_url

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))