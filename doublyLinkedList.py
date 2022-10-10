class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None;
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    def counting_nodes(self):
        n = self.start_node
        t=0
        while n is not None:
            t=t+1
            n=n.next
        print(f"No of nodes is {t}") 
            
    # Traversing and Displaying each element of the list
    def duplicate(self):
        lis2=[]
        n = self.start_node
        while n is not None:
            if n.item in lis2:
                n.prev.next=n.next
            else:
                
                lis2.append(n.item)
                
                
            n=n.next
        # for i in range(len(lis2)):
        #     print(f"Element is: {lis2[i]}")
        self.Display()
        
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")
# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
n=int(input("Enter the no nodes\n"))
lis=[]
print("Enter the element\n")
for i in range(n):
    a=int(input())
    lis.append(a)
NewDoublyLinkedList.InsertToEmptyList(lis[0])
# Insert the element at the end
for i in range(1,n):
    
    NewDoublyLinkedList.InsertToEnd(lis[i])


NewDoublyLinkedList.Display()
# Counting the nodes
NewDoublyLinkedList.counting_nodes()
# Deleting last two elements
NewDoublyLinkedList.delete_at_end()
NewDoublyLinkedList.delete_at_end()
print("After deleting element\n")
# Counting the nodes
NewDoublyLinkedList.counting_nodes()
# Display Data
NewDoublyLinkedList.Display()
# removing duplicate
print("\nRemoving duplicate\n")
NewDoublyLinkedList.duplicate()




