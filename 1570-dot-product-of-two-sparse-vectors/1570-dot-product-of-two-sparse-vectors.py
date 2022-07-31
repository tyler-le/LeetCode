class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.nums
        v2 = vec.nums
        
        v2_pointer = 0
        res = 0
        for v1_pointer in range(len(self.nums)):
            res += (self.nums[v1_pointer] * v2[v2_pointer])
            v2_pointer += 1
        return res
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)