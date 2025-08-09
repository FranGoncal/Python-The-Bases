class Node:
    # constructor method
    def __init__(self, val):
        self.value = val
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self,val):
        self.head = Node(val)
        self.tail = self.head

    def append(self, val):
        self.tail.next = Node(val)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

    def preappend(self, val):
        newHead = Node(val)
        newHead.next = self.head
        self.head.previous = newHead
        self.head=newHead

    def insert(self,pos,val):
        current = self.head

        for i in range(0,pos-1):
            current = current.next
        
        newNode = Node(val)

        if pos == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        elif current.next == None:
            newNode.previous = self.tail
            self.tail = newNode
            current.next = newNode
        else:
            newNode.next = current.next
            current.next.previous = newNode
            newNode.previous = current
            current.next = newNode

    def remove(self,pos):
        if pos == 0:
            self.head= self.head.next
            return
        current = self.head
        for i in range(0,pos-1):
            if current.next==None:
                return
            current = current.next

        if current.next!=None and current.next.next!=None:
            current.next.next.previous= current
            current.next=current.next.next
        else:
            self.tail = current
            current.next = None
            
    def toString(self):
        current = self.head

        s = str(current.value)
        
        while current.next != None: 
            current = current.next
            s += "->" + str(current.value)
    
        print(s)

    def toStringReverse(self):
        current = self.tail

        s = str(current.value)
        
        while current.previous != None: 
            current = current.previous
            s += "->" + str(current.value)
    
        print(s)
    


link = DoubleLinkedList(1)
link.append(2)
link.append(3)
link.append(4)
link.preappend(777)
link.insert(5,14)


link.toString()
link.toStringReverse()

link.remove(5)

link.toString()
link.toStringReverse()


