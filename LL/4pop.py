class node():
    def __init__( self,value):
        self.value = value
        self.next =None

class LinkedList():
    def __init__(self,value):
         new_node= node(value)
         self.head = new_node
         self.tail = new_node
         self.length =1

    def append(self,value):
         self.value = value
         new_node =node(value)
         if self.head is None:
             self.head = new_node
             self.tail = new_node

         else:
             self.tail.next = new_node 
             self.tail = new_node
         self.length +=1    

    def pop(self,value):

        if self.head is None:
            return False
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = None

            
            self.length -=1


             


