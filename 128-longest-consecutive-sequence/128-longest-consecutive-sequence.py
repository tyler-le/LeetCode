class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for num in nums:
            # check if leftmost elem in set
            if num-1 in nums:
                continue
            
            curr_num = num
            count = 0
            while curr_num in nums:
                count +=1
                curr_num+=1
            longest = max(longest, count)
            
        return longest