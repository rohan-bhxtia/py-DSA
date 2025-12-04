class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self,value):
        self.value = value
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
###

    def append(self,value):
        new_node=node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def popFirst(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            self.head  = self.head.next
            temp.next = None
            
        return temp    
    
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next



ll = linkedlist(23)
ll.append(34)
ll.append(54)                

ll.print()

pF= ll.popFirst()
print("popped item: ", pF.value)

ll.print()

                        


