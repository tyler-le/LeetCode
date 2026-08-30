class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [-1 if x == 0 else 1 for x in nums]

        prefix_sums = defaultdict(int)
        prefix_sums[0] = -1
        curr_sum = 0
        res = 0


        for i in range(len(arr)):
            num = arr[i]
            curr_sum+=num
            if curr_sum in prefix_sums:
                res = max(res, i - prefix_sums[curr_sum])
            else:
                prefix_sums[curr_sum] = i
        return res


