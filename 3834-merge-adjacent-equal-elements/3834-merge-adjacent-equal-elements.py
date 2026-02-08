class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        res = []
        stack = []
        
        for num in nums:
            curr = num

            while stack and stack[-1] == curr:
                stack.pop()
                curr*=2
                
            stack.append(curr)

        return stack