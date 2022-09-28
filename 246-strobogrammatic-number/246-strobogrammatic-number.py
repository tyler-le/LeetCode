class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        hmap = {0:0, 6:9, 9:6, 8:8, 1:1}
        
        l, r = 0, len(num)-1
        
        while l < r:
            if int(num[l]) not in hmap or int(num[l]) not in hmap:
                return False
            if hmap[int(num[l])] != int(num[r]): return False
            l+=1
            r-=1
            
        if l == r:
            if int(num[l]) == 1 or int(num[l]) == 8 or int(num[l]) == 0: return True
            return False
        return True