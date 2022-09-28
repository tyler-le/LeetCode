class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        if digits == "": return []
        
        def backtrack(index, combination):
            # base case
            if len(combination) == len(digits):
                res.append("".join(combination))
                return
        
            '''
            loop thu each char in the corresponding digit and perform   
            backtracking on the next digit and its chars
            '''
            
            # letters that the current digit maps to
            possible_letters = letters[digits[index]]
            
            for ch in possible_letters:
                # add to current path
                combination.append(ch) 
                
                # move to next digit
                backtrack(index+1, combination) 
                
                # remove from current path
                combination.pop()
                
        digits = [int(d) for d in str(digits)]
        backtrack(0, [])
        
        return res