

class HashTable:
    # constructor method
    def __init__(self, tamanho):
        self.data = [None] * int(tamanho)


    def set(self, key,value):

        pos = self.hash_in_interval(key)
        if (self.isEmpty(pos)):
            self.data[pos]=[]

        self.data[pos].append([key,value])


    def get(self, key):
        pos = self.hash_in_interval(key)
        bucket = self.data[pos]
        if bucket!=None:
            for i in range(0,len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return 
    
    def isEmpty(self, key):
        pos = self.hash_in_interval(key)
        bucket = self.data[pos]
        return bucket == None


    def hash_in_interval(self, value):
        start = 0
        end = len(self.data)
        raw_hash = hash(value)
        size = end - start #+ 1
        normalized_hash = raw_hash % size
        return start + normalized_hash 
    
    def keys(self):
        keys = []
        for i in range(0,len(self.data)):
            if(self.data[i]!=None):
                for j in range(0,len(self.data[i])):
                    keys.append(self.data[i][j][0])
        return keys
    
    def values(self):
        values = []
        for i in range(0,len(self.data)):
            if(self.data[i]!=None):
                for j in range(0,len(self.data[i])):
                    values.append(self.data[i][j][1])
        return values



hashing = HashTable(3)

hashing.set("grapes",22)
hashing.set("Pineapple",55)
hashing.set("Banana",33)
hashing.set("Pear",276)


print(hashing.get("Pear"))
print(hashing.get("Banana"))


print("\n\n------------\n\n")


print(hashing.keys())
print(hashing.values())