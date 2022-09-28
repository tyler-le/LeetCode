class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hmap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        if digits == "": return []
        def backtrack(index, combination):
            if len(combination) > len(digits): 
                return
            
            elif len(combination) == len(digits):
                res.append("".join(combination))
                return
            
            for ch in hmap[digits[index]]:
                combination.append(ch)
                backtrack(index+1, combination)
                combination.pop()
                
                
                
        digits = [int(d) for d in str(digits)]
        backtrack(0, [])
        return res