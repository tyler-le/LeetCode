class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = {}
        res = []
        
        for num in nums2:
            
            while stack and stack[-1] < num:
                hmap[stack.pop()] = num
            
            stack.append(num)
            
        for num in nums1:
            if num not in hmap:
                res.append(-1)
            else:
                res.append(hmap[num])
        
        return res

    
    [6,5,4,3,2,]