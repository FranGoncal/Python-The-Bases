import json 

class Node:
  def __init__(self, val): 
    self.left = None
    self.right = None
    self.value = val
  


class BinarySearchTree:
    def __init__(self) :
        self.root = None
  
    def insert(self, value):
        current = self.root

        if current == None:
            self.root = Node(value)
            return
        else:
            node = Node(value)
            while True:
                if current.right == None and current.value < value:
                    current.right = node
                    return 
                elif current.left == None and current.value >= value:
                    current.left = node
                    return 
                
                elif current.value < value:
                    current = current.right
                elif current.value > value:
                    current = current.left

                elif current.left.value > value :
                    current = current.left
                elif current.right.value < value:
                    current = current.right
    


    def lookup(self, value):
        current = self.root

        while True:
            if current.value == value:
                return current
            elif (current.value < value and current.right == None) or (current.value > value and current.left == None):
                return None
            elif current.value < value:
                current = current.right
            elif current.value > value:
                current = current.left
            
    
  
    def remove(self, value):
    '''
        current = self.root

        if current.value == value:
            nextCurrent = current.right
            while nextCurrent.left != None:
                nextCurrent = nextCurrent.left
            

            nextCurrent.left = self.root.left
            nextCurrent.right = self.root.right


            return

        
        while True:
            if current.value == value:
                return current
            elif (current.value < value and current.right == None) or (current.value > value and current.left == None):
                return None
            elif current.value < value:
                current = current.right
            elif current.value > value:
                current = current.left

        return'''
  


def traverse(node):
    if node is None:
        return None

    tree = {"value": node.value}
    tree["left"] = traverse(node.left) if node.left is not None else None
    tree["right"] = traverse(node.right) if node.right is not None else None

    return tree


tree = BinarySearchTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.remove(170)
print(json.dumps(traverse(tree.root), indent=2))
print(tree.lookup(20).value)


'''

      9
  4      20
1   6  15  170

'''


