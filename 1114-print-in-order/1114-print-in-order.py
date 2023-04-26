from threading import Lock

class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()
        


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.firstJobDone.locked():
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondJobDone.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.secondJobDone.locked():
            continue
            
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
        