
class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self, value):
        new_node = Node(value)

        if (self.rare == None):
            self.front = new_node
            self.rare = self.front
        else:
            self.rare.next = new_node
            self.rare = new_node

    def dequeue(self):

        if (self.front == None):
            return print("Empty queue")
        self.front = self.front.next

    def traverse(self):

        if (self.front == None):
            return print("Empty queue")
        
        curr = self.front
        while (curr != None):
            print(curr.data, end=' ') 
            curr = curr.next
        print(end='\n') 

Q = Queue()
Q.dequeue()
Q.enqueue(2)
Q.enqueue(4)
Q.enqueue(6)
Q.enqueue(8)
Q.traverse()
Q.dequeue()
Q.dequeue()
Q.traverse()


