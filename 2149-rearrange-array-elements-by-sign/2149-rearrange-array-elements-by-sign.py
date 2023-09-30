class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        res = []
        j, k = 0, 0
        
        for num in nums:
            if num < 0: negatives.append(num)
            else: positives.append(num)
                
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(positives[j])
                j+=1
            else:
                res.append(negatives[k])
                k+=1
        
        return res
            