class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        mx = max(damage)
        without_mx = sum(damage) - mx
        mx_with_armor = max(mx - armor, 0)

        return 1 + without_mx + mx_with_armor
