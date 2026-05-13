class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []

        def f(index, paths):
            if index == n:
                res.append(["".join(p) for p in paths])
                return


            # include in most recent path
            if paths: 
                paths[-1].append(s[index])
                # early prune if added char is not a palindrome
                if paths[-1] == paths[-1][::-1]:
                    f(index + 1, paths)
                paths[-1].pop()
            
            # create a new path
            paths.append([s[index]])
            # early prune if added char is not a palindrome
            f(index + 1, paths)
            paths.pop()

        f(0, [])
        return res

            
            
            
