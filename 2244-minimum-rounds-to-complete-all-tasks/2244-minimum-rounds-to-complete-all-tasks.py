class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count, res = Counter(tasks), 0
        for key, value in count.items():
            print(value)
            if value == 1: 
                return -1
            elif value % 3 == 0:
                res+=(value/3)
            else:
                res+=(value//3 + 1)
        return int(res)
        