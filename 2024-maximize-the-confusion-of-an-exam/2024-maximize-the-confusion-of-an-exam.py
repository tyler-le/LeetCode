class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        num_changes = 0
        l = 0
        res = 0
        
        # change F -> T
        for r in range(len(answerKey)):
            if answerKey[r] == "F": 
                num_changes+=1
            
            while num_changes > k:
                if answerKey[l] == "F": 
                    num_changes-=1
                l+=1    
            
            res = max(res, r-l+1)
            
        num_changes = 0
        l = 0

        # change T -> F
        for r in range(len(answerKey)):
            if answerKey[r] == "T": 
                num_changes+=1

            while num_changes > k:
                if answerKey[l] == "T": 
                    num_changes-=1
                l+=1    

            res = max(res, r-l+1)

        return res