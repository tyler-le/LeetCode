class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []

        def is_pal(l, r):
            while l <= r:
                if s[l] != s[r]: return False
                l+=1
                r-=1
            return True
        
        """
        The comments below are for example "aab"
        """
        def f(start, path):

            if start == n:
                res.append(path.copy())
                return

            for end in range(start, n):

                # if s[start:end+1] is a palindrome (i.e. "aa")
                if is_pal(start, end):

                    # add s[start:end+1] to path (i.e. path = ["aa"])
                    path.append(s[start:end+1])

                    # recurse on s[end+1:] (i.e. recurse on "b")
                    # this call will then append "b" to path
                    # so now path = ["aa", "b"]
                    f(end + 1, path)

                    # undo choice
                    path.pop()
        
        f(0, [])
        return res
            