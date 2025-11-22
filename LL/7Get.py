class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1
##e
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1      

    def Get(self,index):
        if index <0 or index >= self.length :
            return None
        temp = self.head
        for i in range (index):
            temp = temp.next
        return temp    
    

ll = linkedlist(22)
ll.append(3)
ll.append(44)

get= ll.Get(0)
print(get.value)






