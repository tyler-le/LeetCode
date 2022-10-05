class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []

        for log in logs:
            if log.split()[1].isdigit(): digit_logs.append(log) 
            else: letter_logs.append(log)
                
        # first sort by contents. if ties, sort by identifier
        letter_logs.sort(key = lambda i : (i.split(' ')[1:], i.split()[0]))
        
        return letter_logs + digit_logs
     