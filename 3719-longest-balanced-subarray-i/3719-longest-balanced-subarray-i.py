class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            even_map = defaultdict(int)
            odd_map = defaultdict(int)

            for j in range(i, n):
                num = nums[j]
                if num % 2: odd_map[num]+=1
                else: even_map[num]+=1
            
                if len(even_map.values()) == len(odd_map.values()):
                    res = max(res, j-i+1)
        return res