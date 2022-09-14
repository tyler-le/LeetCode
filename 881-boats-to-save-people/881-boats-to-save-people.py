class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        people.sort()
        res = 0
        
        l, r = 0, len(people)-1
        
        while l <= r:
            # put heavy people[r] on boat
            if people[l] + people[r] > limit:
                r-=1
                
            # put both people on boat
            else:
                l+=1
                r-=1
                
            res+=1
        return res
        