class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):#.
        new_node = Node(value)
        if self.head is None:
            return None
        if self.head is self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
##
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def insert(self,value,index):
        new_node = Node(value)
        self.index = index 

        temp = self.head
        for i in range (index):
            temp = temp.next
        temp = new_node
        new


                   
                        


