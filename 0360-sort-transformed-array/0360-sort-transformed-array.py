class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        def f(x):
            first = a * x**2
            second = b * x
            third = c
            return first + second + third

        if a > 0:
            res = deque()
            l, r = 0, len(nums) - 1

            while l <= r:
                left = f(nums[l])
                right = f(nums[r])

                if left > right:
                    res.appendleft(left)
                    l+=1
                else:
                    res.appendleft(right)
                    r-=1
            
            return list(res)

        elif a < 0:
            res = deque()
            l, r = 0, len(nums) - 1

            while l <= r:
                left = f(nums[l])
                right = f(nums[r])

                if left < right:
                    res.append(left)
                    l+=1
                else:
                    res.append(right)
                    r-=1
            
            return list(res)

        else:
            res = deque()
            for num in nums:
                res.append(f(num))
            
            if b > 0: return list(res)
            else: return list(res)[::-1]


