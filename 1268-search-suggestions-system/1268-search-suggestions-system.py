class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        res = []
        products.sort()
        n = len(products)
        m = len(searchWord)

        def binary_search(prefix):

            left_bound, right_bound = None, None

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
            
            # find right bound
            low, high = 0, n-1
            while low < high:
                mid = (low + high + 1) // 2

                word = products[mid]

                if prefix < word[:len(prefix)]:
                    high = mid - 1
                elif prefix > word[:len(prefix)]:
                    low = mid + 1
                else:
                    low = mid

            if products[low][:len(prefix)] == prefix:
                right_bound = low

            return [left_bound, right_bound]
                
                

        # sort
        # for every prefix, binary search for that prefix

        print(products)

        for i in range(1, m + 1):
            prefix = searchWord[:i]
            l, r = binary_search(prefix)
            if l is None or r is None: res.append([])
            else: res.append(products[l:r+1] if r+1-l <= 3 else products[l:l+3])

        return res
