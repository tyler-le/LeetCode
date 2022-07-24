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
            boxes_to_take = min(truckSize, num_boxes)
            res += boxes_to_take * num_units
            truckSize -= boxes_to_take
            
            if truckSize == 0: return res
            
        return res