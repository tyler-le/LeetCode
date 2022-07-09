class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        constructed = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l,r = 0, len(constructed)-1

        while l < r:
            
            if constructed[l] != constructed[r]:
                return False
            
            l+=1
            r-=1
            
        return True
        
        
        