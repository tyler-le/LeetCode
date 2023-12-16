class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hmap = defaultdict(list)

        for i in range(n):
            hmap[nums[i]].append(i)

        for num, indices in hmap.items():
            if len(indices) < 2: continue
            for i in range(1, len(indices)):
                if indices[i] - indices[i-1] <= k: 
                    return True

        return False