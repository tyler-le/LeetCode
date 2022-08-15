class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds, evens, count = {}, {}, Counter(s)
        
        
        # separate even counts from odds
        for key, value in count.items():
            if value % 2 == 0: evens[key] = value
            else: odds[key] = value
                
        max_odd = max(odds.values()) if odds else 0
        res = max_odd 
        
        if odds: del odds[max(odds, key=odds.get)]
              
        res = res + sum(evens.values()) + (sum(odds.values()) - len(odds))
            
        return res