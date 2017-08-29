class Node:

    def __init__(self,v=None):
        self.value = v
        self.next=None

    
    def isempty(self):
        return (self.value == None)

    #iteratively append
    def appendi(self,v):
        if self.isempty():
            self.value = v

        else:
            temp = self
            while temp.next != None:
                temp = temp.next
            
            newnode = Node(v)
            temp.next = newnode

        return

    
    #recursively append
    def append(self,v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.append(v)

        return

    #iteratively delete first occurence of v
    def deletei(self,v):
        if self.isempty():
            return
        if self.value == v:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
            return
       
        temp = self
        while temp.next != None:
            if temp.next.value == v:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next
        return

    #recursively delete first occurence of v
    def delete(self,v):
        if self.isempty():
            return
        if self.value == v:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
            return

        if self.next != None:
           self.next.delete(v)
           if self.next.value == None:
               self.next = None
        
        return

    #insert a value in the first
    def insert(self,v):
        if self.isempty():
            self.value = v
            return

        newnode = Node(v)
        (self.value,newnode.value) = (newnode.value,self.value)
        (self.next,newnode.next) = (newnode,self.next)

        return

    #print
    def __str__(self):
        selflist = []
        if self.value == None:
            print(str(selflist))

        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)    
            
        return str(selflist)
    
