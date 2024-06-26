class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hmap, res, alph = {' ': ' '}, "", 97
        
        # map each letter in key to nth letter of the alphabet
        for k in key:
            if k not in hmap: 
                hmap[k] = chr(alph)
                alph+=1
            
        # decode msg using map
        for m in message:
            res+=(hmap[m])
            
        return res
            
      