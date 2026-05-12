class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1

        for p3 in range(n+m-1, -1, -1):

            # compare nums1[p1] and nums2[p2]

            # nothing left to merge in nums2
            if p2 < 0: break

            # nothing left to merge in nums1 (but still stuff in nums2)
            if p1 < 0: 
                nums1[p3] = nums2[p2]
                p2-=1

            # pull from nums2
            elif nums2[p2] >= nums1[p1]:
                nums1[p3] = nums2[p2]
                p2-=1

            # pull from nums1
            else:
                nums1[p3], nums1[p1] = nums1[p1], nums1[p3]
                p1-=1
        

        