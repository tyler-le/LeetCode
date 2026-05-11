class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # binary search on health and verify

        low, high = 0, sum(damage) + 1
        res = -1


        def valid(health):
            mx = max(damage)
            armor_used = False

            for dmg in damage: 
                if dmg == mx and not armor_used:
                    health-=max(dmg-armor, 0)
                    armor_used = True
                else:
                    health-=dmg
            return health >= 1

           
               


        while low <= high:
            mid = low + ((high - low) // 2)

            if valid(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res