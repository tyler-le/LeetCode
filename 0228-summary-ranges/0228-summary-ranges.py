class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        prev_interval = [nums[0], nums[0]]
        res = []

        for num in nums[1:]:

            prev_start, prev_end = prev_interval

            # 1. add it to current interval?
            if prev_end + 1 == num:
                prev_interval = [prev_start, num]

            # 2. start a new interval?
            else:
                if prev_start == prev_end: 
                    res.append(f"{prev_start}")
                else: 
                    res.append(f"{prev_start}->{prev_end}")

                prev_interval = [num, num]
        

        prev_start, prev_end = prev_interval
        if prev_start == prev_end: res.append(f"{prev_start}")
        else: res.append(f"{prev_start}->{prev_end}")
        return res