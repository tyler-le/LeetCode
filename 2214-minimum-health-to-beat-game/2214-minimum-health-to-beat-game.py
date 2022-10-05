class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        
        # get all occurrences where we WONT use armor
        dmg_without_max = sum(damage) - max_damage
        
        # get the occurrence where we DO use armor
        # return the max of max_damage - armor or 0 (if armor > max_damage)
        use_armor = max(max_damage - armor, 0)
        
        return dmg_without_max + use_armor + 1
    