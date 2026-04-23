class Solution:
    def distance(self, nums: List[int]) -> List[int]:        

        hmap = defaultdict(list) # (value : list of indices)
        prefix_sums = defaultdict(list) # (value : prefix_sums)
        n = len(nums)
        res = [0 for _ in range(n)]

        for i in range(n):
            hmap[nums[i]].append(i)
        
        for x, indices in hmap.items():
            acc = 0
            for index in indices:
                acc+=index
                prefix_sums[x].append(acc)
        
        
        for key, indices in hmap.items():
            if len(indices) <= 1: continue

            for i in range(len(indices)):
                j = indices[i] 

                before = prefix_sums[key][i-1] if i-1 >= 0 else 0
                left = j * i - before

                after = prefix_sums[key][len(indices) - 1] - prefix_sums[key][i]
                right = after - j * (len(indices) - i - 1)

                res[j] = left + right

        return res