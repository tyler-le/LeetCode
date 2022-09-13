class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        for x_query, y_query, radius in queries:
            count = 0
            for x_point, y_point in points:
                # calculate dist from center of query to point
                dist = math.sqrt((x_query - x_point)**2 + (y_query - y_point)**2)
                
                # if distance is less than radius, it is within the query circle
                if dist <= radius: count+=1
            res.append(count)
            
        return res
            