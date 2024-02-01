class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        

        hand.sort()
        res = []
        n = len(hand)
        hmap = Counter(hand)
    
        
        for num in hand:
            # Skip this iteration if the current card count is zero 
            # since it has previously been allocated
            if not hmap[num]: continue
        
            # Attempt to form a group starting from the current card
            for i in range(num, num+groupSize):
                 
                # Required card for the group is missing or depleted
                if i not in hmap or not hmap[i]: return False
                
                # Else use the code
                else: hmap[i]-=1
        
        return True
            