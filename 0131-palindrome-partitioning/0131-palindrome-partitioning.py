class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []

        def f(index, paths):
            if index == n:
                # only the last group is unvalidated at this point
                if not paths[-1] == paths[-1][::-1]:
                    return
                res.append(["".join(p) for p in paths])
                return


            # include in most recent path
            if paths: 
                paths[-1].append(s[index])
                f(index + 1, paths)
                paths[-1].pop()
            
            # create a new path

            # early prune if prev substring was not a palindrome
            if not paths or paths[-1] == paths[-1][::-1]:
                paths.append([s[index]])
                f(index + 1, paths)
                paths.pop()

        f(0, [])
        return res

            
            
            
