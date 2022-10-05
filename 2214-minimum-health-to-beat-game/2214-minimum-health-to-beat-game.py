class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxi = max(damage)
        health = 0
        
        dmg_without_maxi = sum(damage) - maxi
        use_armor = max(maxi-armor, 0)
        
        return dmg_without_maxi + use_armor + 1
        
        
        armor_used = False
        for dmg in damage:
            if dmg == maxi:
                if not armor_used:
                    armor_used = True
                    health+=(max(dmg - armor, 0))
                else:
                    health+=dmg
            else:
                health+=dmg
                
        
        return health+1