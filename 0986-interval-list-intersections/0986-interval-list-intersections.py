class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        n, m = len(firstList), len(secondList)
        res = []

        while p1 < n and p2 < m:
            p1_start, p1_end = firstList[p1]
            p2_start, p2_end = secondList[p2]

            has_overlap = (p2_start <= p1_start <= p2_end) or (p1_start <= p2_start <= p1_end)

            if has_overlap:
                res.append([max(p1_start, p2_start), min(p1_end, p2_end)])
            
            # move pointer with smaller end time
            if p1_end < p2_end: p1+=1
            else: p2+=1
        
        return res

