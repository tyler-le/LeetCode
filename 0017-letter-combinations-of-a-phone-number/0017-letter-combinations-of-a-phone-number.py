class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 2 -> [a, b, c]
        # 3 -> [d, e, f]
        # 4 -> [g, h, i]

        # "234"

        # a + all combinations of "34"
        # b + all combinations of "34"

        hmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(index, path):
            nonlocal res

            # base case
            if index == len(digits): 
                res.append("".join(path.copy()))
                return 

            for choice in hmap[digits[index]]:
                
                path.append(choice)

                backtrack(index + 1, path)

                path.pop()

            
                

        
        backtrack(0, [])
        return res
