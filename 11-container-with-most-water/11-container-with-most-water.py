class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_amount = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            leng = r-l
            heig = min(height[l], height[r])
            area = leng*heig
            max_amount = max(max_amount, area)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
                
        return max_amount