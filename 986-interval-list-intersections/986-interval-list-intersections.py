class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        i,j = 0,0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            # check if the 'start' lies within the other interval
            first_overlaps_second = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            second_overlaps_first = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]
            
            # if so, append overlapping interval
            if first_overlaps_second or second_overlaps_first:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                
            # choose which interval to move onto since the longer one can overlap with another
            if firstList[i][1] < secondList[j][1]:
                i+=1
                
            else:
                j+=1
                
            
        return res
                
            
                
                