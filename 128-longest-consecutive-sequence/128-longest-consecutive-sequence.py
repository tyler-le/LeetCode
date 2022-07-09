class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        
        for num in nums:
            # check if leftmost elem in set
            if num-1 in my_set:
                continue
            
            curr_num = num
            count = 0
            while curr_num in my_set:
                count +=1
                curr_num+=1
            longest = max(longest, count)
            
        return longest