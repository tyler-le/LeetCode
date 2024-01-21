class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        sum_damage = sum(damage)
        max_dmg = max(damage)
        
        no_armor = sum_damage - max_dmg
        yes_armor = max(max_dmg - armor, 0)
        
        return no_armor + yes_armor + 1