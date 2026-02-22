from fractions import Fraction
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        k = Fraction(k)
        operations = ["MUL", "DIV", "NOTHING"]
        cache = {} # (index, curr_val) -> num ways
        
        def backtrack(index, curr_val):

            res = 0

            if (index, curr_val) in cache: 
                return cache[(index, curr_val)]

            if index == len(nums):
                if curr_val == k:
                    res+=1
                    return 1
                return 0
      
            for op in operations:
                if op == "MUL":
                    res+=backtrack(index + 1, curr_val * nums[index])
                elif op == "DIV":
                    res+=backtrack(index + 1, curr_val / nums[index])
                else:
                    res+=backtrack(index + 1, curr_val)

            cache[(index, curr_val)] = res
            return res

        return backtrack(0, Fraction(1))

        