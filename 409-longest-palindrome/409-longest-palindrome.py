class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds, evens, count = {}, {}, Counter(s)
        
        # separate even counts from odds
        for key, value in count.items():
            if value % 2 == 0: evens[key] = value
            else: odds[key] = value
        
        # get the max odd. this will be the middle of our palindrome
        max_odd = max(odds.values()) if odds else 0
        res = max_odd 
        
        # then delete that max_odd from dict
        if odds: del odds[max(odds, key=odds.get)]
           
        # then we can perform the remainder of the palindrome by subtracting 1 from all the values in the odds dict and adding all the evens. 
        # equivalently, we can perform this calculation
        res = res + sum(evens.values()) + (sum(odds.values()) - len(odds))
            
        return res