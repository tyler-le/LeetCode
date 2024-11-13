class TwoSum:

    def __init__(self):
        self.q = []
        

    def add(self, number: int) -> None:
        self.q.append(number)
        

    def find(self, value: int) -> bool:
        seen = set()
        for num in self.q:
            if value - num in seen: 
                return True
            seen.add(num)
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)