class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = deque(popped)
        pushed_stack = []
        
        for num in pushed:
            pushed_stack.append(num)
            while pushed_stack and popped and pushed_stack[-1] == popped[0]:
                popped.popleft()
                pushed_stack.pop()
        
        return not pushed_stack
                