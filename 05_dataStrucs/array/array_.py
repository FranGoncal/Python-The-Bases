strings = ['a','b','c','d']
#1 char -> 4 bytes
#4*4 bytes of memory


#append
strings.append('e') #Time complexity O(1)

#pop
strings.pop() #Time complexity O(1)
strings.pop() #Time complexity O(1)

#insert
strings.insert(0,'x') #Time complexity O(n)
strings.insert(2,'alien') #Time complexity O(n)

print(strings)