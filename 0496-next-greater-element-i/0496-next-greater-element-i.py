class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # map from num1 : index in nums 2
        hmap = {}
        nums2_max = max(nums2)
        nums1_set = set(nums1)
        res = []
        for i, num in enumerate(nums2):
            if num in nums1_set:
                hmap[num] = i


        for num in nums1:
            index_2 = hmap[num]
            found = False
            for i in range(index_2 + 1, len(nums2)):
                if nums2[i] > num:
                    res.append(nums2[i])
                    found = True
                    break
            if not found: res.append(-1)

        return res