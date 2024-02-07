class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(x):
            hmap = defaultdict(int)
            res = 0
            l = 0
            n = len(nums)

            for r in range(n):
                hmap[nums[r]]+=1

                while len(hmap) > x:
                    hmap[nums[l]]-=1
                    if not hmap[nums[l]]: del hmap[nums[l]]
                    l+=1

                res += (r-l+1)

            return res
        
        return at_most(k) - at_most(k-1)