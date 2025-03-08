
class Node:
    
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    
    def __init__(self):
        # Empty Linked list
        self.head = None

        # No. of nodes in LL
        self.n = 0  

    def __len__(self):
        return self.n
    
    def insert_head(self, value):

        # create a new node
        new_node = Node(value)

        # create a connection
        new_node.next = self.head

        # Assigning head
        self.head = new_node

        # increment n
        self.n = self.n + 1

    def __str__(self):

        curr = self.head

        result = ""
        while (curr != None):
            # print(curr.data)
            result = result + str(curr.data) + "->"
            curr = curr.next
        result = result[:-2]

        return result
    
    def append(self, value):

        # create a new node
        new_node = Node(value)

        curr = self.head

        if (curr == None):
            self.head = new_node
        else:
            # traverse LL to last node
            while (curr.next != None):
                curr = curr.next
            curr.next = new_node
        
        # increment n
        self.n = self.n + 1

    def insert_after(self, after, value):

        new_node = Node(value)

        curr = self.head

        while (curr != None):
            if (curr.data == after):
                break
            curr = curr.next

        if (curr != None):
            new_node.next = curr.next
            curr.next = new_node
        else:
            return print("Item not found!!!")
        
    def clear(self):

        self.head = None
        self.n = 0

    def delete_head(self):

        # if empty LL
        if (self.head == None):
            return print("LL is empty")
        
        self.head = self.head.next

        self.n = self.n - 1

    def pop(self):

        # if empty LL
        if (self.head == None):
            return print("LL is empty")
        
        curr = self.head

        if (curr.next == None):
            # iska matlb LL mein ek hi item hai and i.e a head
            return self.delete_head()

        while (curr.next.next != None):
            curr = curr.next

        # at this point curr is second last node
        curr.next = None

        self.n = self.n - 1

    def remove(self, value):

        # if empty LL
        if (self.head == None):
            return print("LL is empty")
        
        if (self.head.data == None):
            return self.delete_head()

        curr = self.head

        while (curr.next != None):
            if (curr.next.data == value):
                break
            curr = curr.next

        if (curr.next == None):
            return print("Value not found!!!")
        else:
            curr.next = curr.next.next

    def search(self, item):

        curr = self.head
        pos = 0

        while (curr != None):
            if (curr.data == item):
                return print(pos)
            curr = curr.next
            pos = pos + 1

        return print("Item not found!!!")
    
    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while (curr != None):
            if (pos == index):
                return print(curr.data)
            curr = curr.next
            pos = pos + 1

        return print("Index error")

L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.insert_after(3,6)
L.append(5)
print(len(L))
print(L)
L.delete_head()
L.pop()
L.remove(1)
L.search(30)
L[1]
print(L)