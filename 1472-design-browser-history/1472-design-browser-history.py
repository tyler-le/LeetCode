class Node():
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.position = Node(homepage)
            

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_page = Node(url)
        new_page.prev = self.position
        self.position.next = new_page
        
        self.position = new_page
        
        
                

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.position.prev and steps:
            self.position = self.position.prev
            steps-=1
        return self.position.url
        
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        
        while self.position.next and steps:
            self.position = self.position.next
            steps-=1
        return self.position.url
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)