class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s1_skips, t1_skips = 0,0
        s1,t1 = len(s)-1, len(t)-1
        
        while s1 >= 0 or t1 >= 0:
            while s1>=0:
                if s[s1]=='#':
                    s1_skips+=1
                    s1-=1
                elif s1_skips > 0:
                    s1_skips-=1
                    s1-=1
                else:
                    break
                
            while t1>=0:
                if t[t1]=='#':
                    t1_skips+=1
                    t1-=1
                elif t1_skips > 0:
                    t1_skips-=1
                    t1-=1
                else:
                    break
                
            if s1>=0 and t1>=0 and s[s1]!=t[t1]:
                return False
            
            if (s1 >= 0) != (t1>=0):
                return False
            
            s1-=1
            t1-=1
            
        return True