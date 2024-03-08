class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # counting sort
        # frequencies range from 0 -> len(nums)
        
        n = len(nums)
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        
        return sum(freq for freq in cnt.values() if freq == max_freq)