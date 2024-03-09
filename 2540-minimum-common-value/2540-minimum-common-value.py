class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # two pointer
        
        p1, p2 = 0, 0
        n, m = len(nums1), len(nums2)
        
        while p1 < n and p2 < m:
            
            # increment p1 pointer
            if nums1[p1] < nums2[p2]: p1+=1
                
            # increment p2 pointer
            elif nums1[p1] > nums2[p2]: p2+=1
                
            # found equal
            else: return nums1[p1]
        
        return -1