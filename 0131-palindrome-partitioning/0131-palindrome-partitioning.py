class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []

        def f(index, paths):
            if index == n:
                flag = True
                for x in paths.copy():
                    if x != x[::-1]:
                        return

                sublist = []
                for path in paths.copy():
                    sublist.append("".join(path))
                res.append(sublist)
                return


            # include in most recent path
            if paths: 
                paths[-1].append(s[index])
                f(index + 1, paths)
                paths[-1].pop()
            
            # create a new path
            paths.append([s[index]])
            f(index + 1, paths)
            paths.pop()

        f(0, [])
        return res

            
            
            
