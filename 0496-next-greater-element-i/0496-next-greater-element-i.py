class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # keep a monotonically decreasing stack
        # build the (element, next_greater) of the numbers in nums2 using this stack

        decreasing = []
        next_greater_in_nums_2 = {}

        for num in nums2:

            # with a monotonically decreasing stack
            # the element we popped is greater than num
            # this must mean that popped's next greater element is num
            while decreasing and decreasing[-1] < num:
                smaller = decreasing.pop()
                next_greater_in_nums_2[smaller] = num
            
            decreasing.append(num)
        
        res = []

        for num in nums1:
            if num not in next_greater_in_nums_2: res.append(-1)
            else: res.append(next_greater_in_nums_2[num])

        return res