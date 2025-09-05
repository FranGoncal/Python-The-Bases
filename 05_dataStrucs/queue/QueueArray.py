class QueueArray:
    #constructor method
    def __init__(self):
        self.array = []
        self.lenght = 0

    def peek(self):
        if len(self.array) > 0:
            return self.array[len(self.array)-1]

    def enqueue(self, value):
        arra = self.array[::-1]
        arra.append(value)
        self.array = arra[::-1]

    def dequeue(self):
        return self.array.pop()

    def printQueue(self):
        s = "Inicio\n"
        for i in range(len(self.array)-1,-1,-1):
            s += self.array[i]+"\n"
        print(s+"Fim\n")

queue = QueueArray()
queue.printQueue()

queue.enqueue("google.com")
queue.printQueue()


queue.enqueue("udemy.com")
queue.printQueue()


queue.enqueue("youtube.com")
queue.printQueue()



queue.dequeue()
queue.printQueue()