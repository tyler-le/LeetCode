class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # counting sort
        # frequencies range from 0 -> len(nums)
        
        n = len(nums)
        freqs = [0 for _ in range(n+1)]
        cnt = Counter(nums)
        
        for num, freq in cnt.items():
            freqs[freq]+=freq
        
        for freq in freqs[::-1]:
            if freq: return freq