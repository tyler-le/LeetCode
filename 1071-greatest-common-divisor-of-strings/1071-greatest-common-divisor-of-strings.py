class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        
        def f(smaller, bigger):
            for i in range(len(smaller)-1, -1, -1):
                candidate = smaller[0:i+1]
                
                copies_smaller = len(smaller) // len(candidate)
                copies_bigger = len(bigger) // len(candidate)
                
                if candidate*copies_smaller == smaller and candidate*copies_bigger == bigger:
                    return candidate
            
            return ""
        
        if len(str1) < len(str2): return f(str1, str2)
        else: return f (str2, str1)
            