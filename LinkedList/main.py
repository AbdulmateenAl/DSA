# This represents every data/item in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This displays the property of the linked list in whole
class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head == None: # If the linked list is empty, put the new node as the head
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        curr = self.head
        if curr and curr.data == data:
            self.head = curr.next
            return
        
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        
        if not curr:
            print("Item not found")
            return
        
        prev.next = curr.next
    
    def display(self):
        elements = []

        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print("Linked List: ", elements)

l1 = LinkedList()
l1.add_to_end(1)
l1.add_to_end(2)
l1.add_to_beginning(0)
l1.delete_node(10)
l1.display()