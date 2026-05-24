class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        # max in window is decreasing[0]
        decreasing = deque()

        # min in window is increasing[0]
        increasing = deque()

        l, n, res = 0, len(nums), 1

        for r in range(n):
            # add nums[r] to window
            while decreasing and decreasing[-1] < nums[r]:
                decreasing.pop()

            while increasing and increasing[-1] > nums[r]:
                increasing.pop()

            decreasing.append(nums[r])
            increasing.append(nums[r])

            # shrink window from left
            while decreasing and increasing and decreasing[0] - increasing[0] > limit:
                popped = nums[l]
                if decreasing[0] == popped: decreasing.popleft()
                if increasing[0] == popped: increasing.popleft()
                l+=1

            # record result
            res = max(res, r-l+1)

        return res