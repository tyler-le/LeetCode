class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(len(searchWord)):
            word = searchWord[0:i+1]
            
            #binary search word in products
            low, high = 0, len(products)-1
            
            while low <= high:
                mid = low + (high - low) // 2
                if products[mid] < word: low = mid + 1
                elif products[mid] >= word: high = mid - 1
                    
            curr = []
            for i in range(3):
                if low+i < len(products) and word in products[low + i][0:len(word)]:
                    curr.append(products[low + i])
            res.append(curr)
                        
        return res
                
                
            