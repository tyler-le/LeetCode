class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # answer[0] = all nums in nums1 that are not in nums2
        # answer[1] = all nums in nums2 that are not in nums1
        
        answer = [[], []]
        s1, s2 = set(nums1), set(nums2)
        
        for num in s1:
            if num not in s2:
                answer[0].append(num)
        
        for num in s2:
            if num not in s1:
                answer[1].append(num)
                
        return answer
                
            
        
        