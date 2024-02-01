class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        

        hand.sort()
        res = []
        n = len(hand)
        hmap = Counter(hand)
        print(hmap)
        print(hand)

# Counter({
#      3: 0, 
#      4: 0, 
#      6: 1, 
#      2: 0, 
#      5: 0, 
#      7: 0, 
#      8: 1
#         })

#     [2, 3, 3, 4, 4, 5, 6, 6, 7, 8]
        
        for num in hand:
            if not hmap[num]: continue
        
            for i in range(num, num+groupSize):
                if i not in hmap or not hmap[i]: return False
                else: hmap[i]-=1
        
        return True
            
            
                    
        
            
            
            