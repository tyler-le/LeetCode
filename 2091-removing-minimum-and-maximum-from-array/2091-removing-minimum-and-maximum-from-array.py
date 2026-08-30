class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # largest window without the min/max elems

        l = 0
        n = len(nums)
        mn, mx = min(nums), max(nums)
        window_cnt = defaultdict(int)
        res = 0

        for r in range(n):
            window_cnt[nums[r]]+=1

            while mn in window_cnt or mx in window_cnt:
                window_cnt[nums[l]]-=1
                if not window_cnt[nums[l]]: del window_cnt[nums[l]]
                l+=1
            
            if mn not in window_cnt and mx not in window_cnt:
                res = max(res, r-l+1)

        return n - res