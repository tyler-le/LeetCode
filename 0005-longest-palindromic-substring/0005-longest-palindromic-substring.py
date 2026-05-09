class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)


        # returns longest palindrome 
        def expand_outward(i):
            res = [0,0]

            # check even
            left = i
            right = left + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if (right - left + 1) > (res[1] - res[0] + 1):
                        res = [left, right]
                    left-=1
                    right+=1
                else:
                    break

            # check odd
            left = i
            right = i
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if (right - left + 1) > (res[1] - res[0] + 1):
                        res = [left, right]
                    left-=1
                    right+=1
                else:
                    break

            return res



        res = (0, 0)

        for i in range(n):
            start, end = expand_outward(i)

            if (end - start + 1) > (res[1] - res[0] + 1):
                res = (start, end)
        
        return s[res[0]:res[1] + 1]
