class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        for i in range(n):
            
            
            # left_smaller and left_greater
            left_smaller, left_greater = 0, 0
            for j in range(i):
                if rating[j] < rating[i]: left_smaller+=1
                elif rating[j] > rating[i]: left_greater+=1

            # right_smaller and right_greater
            right_smaller, right_greater = 0, 0
            for k in range(i+1, n):
                if rating[k] < rating[i]: right_smaller+=1
                elif rating[k] > rating[i]: right_greater+=1

            res = res + (left_smaller * right_greater) + (left_greater * right_smaller)
        
        return res
