class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        cnt = Counter(hand)

        for card in hand:
            # only start a sequence if it has cards
            if not cnt[card]: continue

            # check the rest of the sequence for validity
            for i in range(card, card + groupSize):
                if not cnt[i]: return False
                cnt[i]-=1

        return True
               


