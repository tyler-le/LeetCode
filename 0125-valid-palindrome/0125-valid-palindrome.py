class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
            
        return True