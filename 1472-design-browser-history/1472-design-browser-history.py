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
        self.root = Node(homepage)
            

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_page = Node(url)
        new_page.prev = self.root
        self.root.next = new_page
        
        self.root = self.root.next
        
        
                

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.root.prev and steps:
            self.root = self.root.prev
            steps-=1
        return self.root.url
        
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        
        while self.root.next and steps:
            self.root = self.root.next
            steps-=1
        return self.root.url
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)