
class Node:
    
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return (self.top == None)
    
    def push(self, value):

        new_node = Node(value)

        new_node.next = self.top

        self.top = new_node

    def traverse(self):
        curr = self.top

        while (curr != None):
            print (curr.data)
            curr = curr.next

    def pop(self):

        if (self.top != None):
            self.top = self.top.next
        else:
            return print("Empty stack")
        
    def peek(self):

        if (self.top != None):
            print(self.top.data)
        else:
            return print("Empty stack")

S = Stack()
print(S.isEmpty())
S.push(1)
S.push(2)
S.traverse()
S.peek()
S.pop()
S.traverse()
print(S.isEmpty())