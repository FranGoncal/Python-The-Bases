class MyArray:
    # constructor method
    def __init__(self):
        self.tamanho = 0
        self.data = {}

    def get(self, idx):
        return self.data[idx]
    
    def push(self, item):
        self.data[self.tamanho] = item
        self.tamanho += 1
    
    def pop(self):
        last = self.data[self.tamanho-1]
        del self.data[self.tamanho-1]
        self.tamanho -= 1
        return last
    
    def delete(self, idx):
        item = self.data[idx]
        self.shiftItems(idx)
        del self.data[self.tamanho-1]
        self.tamanho -= 1
    def shiftItems(self, idx):
        for i in range(idx, self.tamanho - 1):
            self.data[i] = self.data[i+1]


    # instance method
    def toString(self):
        print(f"tamanho {self.tamanho} data {self.data} .")




arra = MyArray()
print(arra.toString())


arra.push("hi")
arra.push("you")
arra.push("!")
print(arra.toString())


arra.pop()
print(arra.toString())


arra.push("are")
arra.push("awesome")
arra.push("!")
print(arra.toString())


arra.delete(2)
print(arra.toString())
