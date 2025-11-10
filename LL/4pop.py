class node():
    def __init__( self,value):
        self.value = value
        self.next =None

class Linkedlist():
    def __init__(self,value):
         new_node= node(value)
         self.head = new_node
         self.tail = new_node
         self.length =1

    def append(self,value):
         new_node =node(value)
         if self.head is None:
             self.head = new_node
             self.tail = new_node

         else:
             self.tail.next = new_node 
             self.tail = new_node
         self.length +=1    

    def pop(self):

        if self.length == 0:
            print("linked List is already empty")
        if self.head is self.tail:
            temp=self.head 
            self.head = None
            self.tail = None
            self.length -=1
        else:    
         temp = self.head
         pre = self.head
         while temp.next :
            pre = temp
            temp = temp.next
         self.tail = pre
         self.tail.next = None
         self.length -=1
        

        return temp
    
    def print(self):
        temp = self.head
        while temp is not None:
            print("linkedlist: ",temp.value)
            temp = temp.next


             
ll = Linkedlist(23)
ll.print()
pop = ll.pop()
print("popped : ",pop.value)
