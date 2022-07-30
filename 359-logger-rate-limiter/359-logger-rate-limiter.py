class Logger:

    def __init__(self):
        self.log = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(self.log)
        if message not in self.log:
            self.log[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.log[message]:
                self.log[message] = timestamp + 10
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)