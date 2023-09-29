LEFT = 0
HEIGHT = 1
RIGHT = 2

N = int(input())
building_list = [[int(i) for i in input().split(' ')] for _ in range(N)]

def min(p, q):
    if(p > q):
        return q
    else :
        return p

def max(p, q):
    if(p>q):
        return p
    else : 
        return q

class Range_node:

    node_L = None
    node_R = None

    def __init__(self, left, height, right):
        self.left = left
        self.right = right
        self.height = height
    
    def set_node_L(self, node):
        self.node_L = node
    
    def set_node_R(self, node):
        self.node_R = node
    
    
    def add(self, left, height, right):

        if(left == right):
            return
        
        if(left > right):
            return
        

        if(self.right >= left):
            
            if(self.node_R == None):
                self.set_node_R(Range_node(left, height, right))
                return
            
            self.node_R.add(left, height, right)
            return

        if(self.left <= right):

            if(self.node_L == None):
                self.set_node_L(Range_node(left, height, right))

            self.node_L.add(left, height, right)
            return
        
        self.node_L.add(min(self.left, left), 
                        min(self.left, left) == self.left if self.height else height,
                        max(self.left, left))
        self.node_R.add(min(self.right, right), 
                        max(self.right, right) == self.right if self.height else height,
                        max(self.right, right))
        self.left = max(self.left, left)
        self.right = min(self.right, right)
        self.height = max(self.height, height)

