class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        acc = 0
        for x in w:
            acc+=x
            self.prefix_sum.append(acc)

        self.mn = 0
        self.mx = self.prefix_sum[-1] - 1

    def pickIndex(self) -> int:
        index = randint(self.mn, self.mx)
        return bisect_right(self.prefix_sum, index)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
