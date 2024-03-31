class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort in ascending order of attack,
        # If attack is same sort in descending order of defense
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        weakCharacters = 0
        maxDefense = 0
        for i in range(len(properties) - 1, -1, -1):
            # Compare the current defense with the maximum achieved so far
            if properties[i][1] < maxDefense:
                weakCharacters += 1
            maxDefense = max(maxDefense, properties[i][1])
        
        return weakCharacters