class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)
                            
        paragraph = paragraph.split(" ")
        print(paragraph)
        hmap = collections.defaultdict(int)
        banned = set(banned)
        
        for word in paragraph:
            if word.lower() in banned: continue
            if word == '': continue
            hmap[word.lower()]+=1
            
        max_heap = []
        
        for word, freq in hmap.items():
            max_heap.append((-freq, word))
        heapify(max_heap)
        return heappop(max_heap)[1]