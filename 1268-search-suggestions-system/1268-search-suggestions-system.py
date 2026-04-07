class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        res = []
        products.sort()
        n = len(products)
        m = len(searchWord)

        def binary_search(prefix):

            res = []

            # find left bound
            left_bound = bisect_left(products, prefix)

            # scan for right bound
            for i in range(left_bound, min(n, left_bound + 3)):
                    if products[i].startswith(prefix):
                        res.append(products[i])
                

            return res

                
                

        # sort
        # for every prefix, binary search for that prefix
        for i in range(1, m + 1):
            prefix = searchWord[:i]
            res.append(binary_search(prefix))
        

        return res
