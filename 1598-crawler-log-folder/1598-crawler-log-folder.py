class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == '../':
                if depth > 0:  # Can only go back if not at root
                    depth -= 1
            elif log != './':  # This is a move to a child directory
                depth += 1
        return depth