class Tree:
    #Empty node has self.value,self.left,self.right = None
    #leaf has self.value != None and self.left,self.right point to empty node

    #constructor create an empty nodeor a leaf node, depending on initval

    def __init__(self, v = None):
        self.value = v
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    #only empty node has value None
    def isempty(self):
        return (self.value == None)

    #leaf nodes have both children empty
    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())

    #insert value v in tree
    def insert(self,v):
        if (self.isempty()): #Add v as a new leaf
            self.value = v
            self.left = Tree()
            self.right = Tree()

        if self.value == v:
            return #Do nothing. no duplicates in BTree

        if v < self.value:
            self.left.insert(v)
            return

        if v > self.value:
            self.right.insert(v)
            return

    #inorder traversal
    def inorder(self):
        if (self.isempty()):
            return([])
        else:
            return ( self.left.inorder() +
                     [self.value] +
                     self.right.inorder())

    #Display Tree as a string
    #list values in sorted order
    def __str__(self):
        return(str(self.inorder()))

    #Left most node in the tree
    def minval(self):
        #Assuming self is not empty
        if (self.left.isempty()):
            return(self.value)
        else:
            return(self.left.minval())

    #Right most node in the tree
    def maxval(self):
        #Assuming self is not empty
        if (self.right.isempty()):
            return(self.value)
        else:
            return(self.right.maxval())

    #find
    def find(self,v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        else:
            if(v < self.value):
                return(self.left.find(v))
            else:
                return(self.right.find(v))

    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return
    
    def copy_right(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return
    
    #delete v
    def delete(self,v):
        if self.isempty():
            return False

        if v < self.value:
            self.left.delete(v)
            return
        
        if v > self.value:
            self.right.delete(v)
            return
        
        if v == self.value:
            if self.isleaf():
                self.makeempty()

            elif self.left.isempty():
                self.copy_right()

            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
        
