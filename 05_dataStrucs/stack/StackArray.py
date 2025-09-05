class Stack:
    #constructor method
    def __init__(self):
        self.array = []

    '''lets us see the top element'''
    def peek(self):
        return self.array[len(self.array)-1]


    '''lets us add a node to the top'''
    def push(self, content):
        self.array.append(content)
        

    '''lets us remove from the top'''
    def pop(self):
        self.array.pop()


    '''chech if its empty'''
    def isEmpty(self):
        return len(self.array) == 0
    
    def printStack(self):

        s = "//TOP\\\\\n"

        for i in range(0,len(self.array)):
            s += "||"+str(self.array[len(self.array)-i-1])+"||\n"

        print(s+"\\Bottom/\n")




stack = Stack()
stack.printStack()

stack.push("Discord")
stack.printStack()

stack.push("Udemy")
stack.printStack()

print("Peek-> "+stack.peek()+"\n")

stack.push("Google")
stack.printStack()

stack.pop()
stack.printStack()

stack.pop()
stack.printStack()

print("Peek-> "+stack.peek()+"\n")