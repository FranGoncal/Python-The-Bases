class Node:
    # constructor method
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    #constructor method
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0

    '''lets us see the top element'''
    def peek(self):
        return self.top


    '''lets us add a node to the top'''
    def push(self, content):
        newNode = Node(content)
        newNode.next = self.top
        self.top = newNode
        if self.isEmpty():
                self.bottom = newNode
        self.lenght += 1
        

    '''lets us remove from the top'''
    def pop(self):
        if not self.isEmpty():      
            self.top = self.top.next
            if self.lenght == 1:
                self.bottom = None
            self.lenght -= 1 


    '''chech if its empty'''
    def isEmpty(self):
        return self.lenght == 0
    
    def printStack(self):

        s = "//TOP\\\\\n"

        node = self.top
        for i in range(self.lenght):
            s += "||"+str(node.value)+"||\n"
            node = node.next
        print(s+"\\Bottom/\n")




stack = Stack()
stack.printStack()

stack.push("Discord")
stack.printStack()

stack.push("Udemy")
stack.printStack()

print("Peek-> "+stack.peek().value+"\n")

stack.push("Google")
stack.printStack()

stack.pop()
stack.printStack()

stack.pop()
stack.printStack()

print("Peek-> "+stack.peek().value+"\n")