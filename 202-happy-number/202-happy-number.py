class Solution(object):

    def sum_of_squares(self, num):
        sum = 0
        for digit in str(num):
            sum += int(digit) * int(digit)
        return sum
     
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        
        while (True):
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
            
            if slow == 1 or fast == 1:
                return True
            
            elif slow == fast and slow != 1:
                return False
                
    
   
   
            
    
            
            
        