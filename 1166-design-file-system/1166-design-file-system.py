class MultiWayTrieNode():
    def __init__(self, directory):
        self.children = {}
        self.value = -1
        self.dir = directory
        
        
class FileSystem(object):

    def __init__(self):
        self.root = MultiWayTrieNode("root")

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        directories = path.split('/')
        curr = self.root
        path_exists = True
        
        for i in range(1, len(directories)):
            direc = directories[i]
            
            if direc not in curr.children: 
                # if last directory, create new
                if i == len(directories)-1: 
                    curr.children[direc] = MultiWayTrieNode(direc)
                    
                # if not last directory, this IS the missing parent
                else: return False
            
            # advance to next dir
            curr = curr.children[direc]
        
        # path already exists
        if curr.value != -1: return False
        
        # associate value and return true
        curr.value = value
        return True
        
        

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        directories = path.split('/')
        curr = self.root
        
        for direc in directories[1:]:
            if direc not in curr.children: return -1
            curr = curr.children[direc]
        return curr.value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)