class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        

        hand.sort()
        res = []
        n = len(hand)
        hmap = Counter(hand)
    
        
        for num in hand:
            if not hmap[num]: continue
        
            for i in range(num, num+groupSize):
                if i not in hmap or not hmap[i]: return False
                else: hmap[i]-=1
        
        return True
            
            
                    
        
            
            
            