class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        groups = 0
        cnt = Counter(hand)

        for card in hand:
            if not cnt[card]: continue
            is_valid = True

            for i in range(card, card + groupSize):
                if not cnt[i]: 
                    return False
                else:
                    cnt[i]-=1
                    
        return True
