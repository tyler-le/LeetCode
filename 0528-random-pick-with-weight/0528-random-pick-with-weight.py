class Solution:

    def __init__(self, w: List[int]):
        # keep track of total sum
        # map a number to its probability
        acc = 0
        self.prefix_sum = []

        for num in w:
            acc+=num
            self.prefix_sum.append(acc)

    def pickIndex(self) -> int:
        rand_int = randint(0, max(self.prefix_sum) - 1)
        return bisect_right(self.prefix_sum, rand_int)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()