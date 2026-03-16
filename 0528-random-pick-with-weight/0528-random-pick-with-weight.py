class Solution:

    def __init__(self, w: List[int]):
        
        """
        i.e. given [3, 2, 4]

        we *could* build something like [3, 3, 3, 2, 2, 4, 4, 4, 4], pick a random one, and scan left for the index 

        but this is a waste of space

        instead, let's examine the prefix sum

        prefix_sum([3, 2, 4]) = [3, 5, 9]. 

        We can think of these numbers as the bucket. i.e. prefix_sum[0] = 3 means the 0th index ranges from [0...(3-1)]

        so here, each elem in prefix sum [3, 5, 9] represents the right boundary in [3, 3, 3, 2, 2, 4, 4, 4, 4] 

        so we could just pick a random number between [0, 9] and determine which bucket it belongs to
        
        lets say we have random number 2
        
        to find which bucket it belongs to in prefix sum [3, 5, 9], we just bisect_right

        here '2' belongs to the bucket of the 0th index.

        which means index 0 was chosen with probability 3/10. since we chose 2 from a range of [0,9]

        """


        acc = 0
        self.prefix_sum = []

        for num in w:
            acc+=num
            self.prefix_sum.append(acc)

        self.max = max(self.prefix_sum)

    def pickIndex(self) -> int:
        rand_int = randint(0, self.max - 1)
        return bisect_right(self.prefix_sum, rand_int)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()