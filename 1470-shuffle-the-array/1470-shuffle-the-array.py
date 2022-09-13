class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        slow, fast = 0, n
        res = []
        for _ in range(n):
            res.append(nums[slow])
            res.append(nums[fast])
            slow+=1
            fast+=1
        return res
        
            