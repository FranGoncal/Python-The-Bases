class Node:
    # constructor method
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self,val):
        self.head = Node(val)
        self.tail = self.head

    def append(self, val):
        '''while self.head.next != None:
            self = self.next
        self.next = LinkedList(val)'''
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def preappend(self, val):
        newHead = Node(val)
        newHead.next = self.head
        self.head=newHead

    def insert(self,pos,val):
        current = self.head

        for i in range(0,pos-1):
            current = current.next
        
        newNode = Node(val)

        if pos == 0:
            newNode.next = self.head
            self.head = newNode
        elif current.next == None:
            self.tail = newNode
            current.next = newNode
        else:
            newNode.next = current.next
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

        if current.next!=None:
            current.next=current.next.next

    def reverse(self):
        if self.head.next == None:
            return
        
        current= self.head

        self.preappend(current.value)

        self.head.next = None

        while current.next != None:
            current = current.next
            self.preappend(current.value)

    def toString(self):
        current = self.head

        s = str(current.value)
        
        while current.next != None: 
            current = current.next
            s += "->" + str(current.value)
    
        print(s)
    

link = LinkedList(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.append(6)
link.preappend(99)
link.toString()


link.insert(1,88)
link.toString()


link.remove(7)
link.toString()

link.reverse()
link.toString()