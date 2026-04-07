class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        res = []
        products.sort()
        n = len(products)
        m = len(searchWord)

        def binary_search(prefix):

            left_bound, right_bound = None, None
            res = []

            # find left bound
            low, high = 0, n-1
            while low < high:
                mid = (high + low) // 2
                word = products[mid]

                if prefix <= word[:len(prefix)]:
                    high = mid
                else:
                    low = mid + 1

            if products[low][:len(prefix)] == prefix:
                left_bound = low

            if left_bound is None:
                return []
            else:
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
