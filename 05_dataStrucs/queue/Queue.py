class Node:
    # constructor method
    def __init__(self, val):
        self.value = val
        self.next = None


class Queue:
    #constructor method
    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    '''lets us see first'''
    def peek(self):
        return self.first


    '''adds element to the end of the queue'''
    def enqueue(self, content):
        newNode = Node(content)
        if self.lenght == 0:
            self.first = newNode
            self.last = newNode
            
        else:
            self.last.next = newNode
            self.last = newNode
        self.lenght += 1
        

    '''removes the first element in the queue'''
    def dequeue(self):
        if not self.isEmpty():      
            self.first = self.first.next
            self.lenght -= 1


    '''chech if queue is empty'''
    def isEmpty(self):
        return self.lenght == 0
    
    def printStack(self):
        s = "//Start\\\\\n"

        node = self.first
        for i in range(self.lenght):
            s += "||"+str(node.value)+"||\n"
            node = node.next
        print(s+"\\End/\n")




stack = Queue()
stack.printStack()


stack.enqueue("Discord")
stack.printStack()

print("Peek-> "+stack.peek().value+"\n")

stack.enqueue("Udemy")
stack.printStack()

print("Peek-> "+stack.peek().value+"\n")

stack.enqueue("Google")
stack.printStack()

stack.dequeue()
stack.printStack()

stack.dequeue()
stack.printStack()

print("Peek-> "+stack.peek().value+"\n")