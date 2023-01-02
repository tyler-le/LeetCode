class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1: return True
        # if first is capital, we break into two cases
        if word[0].isupper():
        # 1. second is capital, then all must be capital
            if word[1].isupper():
                for w in word:
                    if not w.isupper():
                        return False
        # 2. else no others can be capital
            else:
                for w in word[1:]:
                    if w.isupper():
                        return False
        
        # otherwise, no others can be capital
        else:
            for w in word:
                if w.isupper():
                    return False
        return True
        