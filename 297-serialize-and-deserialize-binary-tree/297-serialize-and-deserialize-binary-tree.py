# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = []
        i=0
        def preorder(root):
            if not root:
                serial.append('Null')
                return
                
            serial.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return ','.join(serial)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        self.i = 0
        
        def preorder():
            if data[self.i] == 'Null':
                self.i+=1
                return None
            
            root = TreeNode(int(data[self.i]))
            self.i+=1
            root.left = preorder()
            root.right = preorder()
            return root
            
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))