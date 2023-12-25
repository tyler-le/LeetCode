class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        alice, bob = 0, 0
        for i in range(1, n-1):
            
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    alice+=1
                else:
                    bob+=1
                
        return alice > bob
                