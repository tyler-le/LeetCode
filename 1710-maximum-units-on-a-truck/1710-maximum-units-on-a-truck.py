class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda i : i[1])
        boxTypes.reverse()
        res = 0
        
        for num_boxes, num_units in boxTypes:
            while truckSize and num_boxes > 0:
                res += num_units
                num_boxes -= 1
                truckSize -= 1
                
            if not truckSize:
                return res
            
        return res