class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         p1 tracks next position of ~val
#         p2 tracks next position of val
#         set nums[p2] = nums[p1]
        
        val_ptr, non_val_ptr = 0, 0
        n = len(nums)
        
        while non_val_ptr < n:
            
            # set val_ptr
            while val_ptr < n and nums[val_ptr] != val:
                val_ptr+=1
            
            non_val_ptr = val_ptr + 1
            
            while non_val_ptr < n and nums[non_val_ptr] == val:
                non_val_ptr+=1
            
            if val_ptr < n and non_val_ptr < n:
                nums[val_ptr], nums[non_val_ptr] = nums[non_val_ptr], nums[val_ptr]
            
        return val_ptr
            
            