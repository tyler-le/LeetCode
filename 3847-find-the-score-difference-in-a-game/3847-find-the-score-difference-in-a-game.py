class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p1_score, p2_score = 0, 0
        curr_turn = "p1"
        n = len(nums)

        for i in range(n):
            if nums[i] % 2:
                if curr_turn == "p1":
                    curr_turn = "p2"
                else:
                    curr_turn = "p1"

            if (i+1) % 6 == 0:
                if curr_turn == "p1":
                    curr_turn = "p2"
                else:
                    curr_turn = "p1"

            if curr_turn == "p1":
                p1_score+=nums[i]
            else:
                p2_score+=nums[i]

        return p1_score - p2_score