class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits)<2:
            return len(fruits)
        
        max_trees = -(sys.maxint-1)
        start,end = 0,1
        my_dict = {}
        
        my_dict[fruits[start]] = 1
        
        while end < len(fruits):
            max_trees = max(max_trees, end-start)
            
            if fruits[end] in my_dict:
                my_dict[fruits[end]]+=1
            else:
                my_dict[fruits[end]]=1
            
            while len(my_dict) > 2:
                if my_dict[fruits[start]]>0:
                    my_dict[fruits[start]]-=1
                
                if my_dict[fruits[start]] == 0:
                    del my_dict[fruits[start]]
                    
                start+=1
                
            end+=1
        
        return max(max_trees, end-start)