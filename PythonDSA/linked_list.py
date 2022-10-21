"""
Linked List implementation with many features, including, append, push, append at position, delete at position, detect cycle, etc.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
    
    def delete_node_at_position(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    def delete_list(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev
        self.head = None
    
    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def get_nth(self, index):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.data
            count += 1
            temp = temp.next
        assert(False)
        return 0
    
    def get_nth_from_last(self, index):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        if length < index:
            return
        temp = self.head
        for i in range(0, length - index):
            temp = temp.next
        return temp.data
    
    def get_middle(self):
        slow = self.head
        fast = self.head
        if self.head is not None:
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow.data
        return None
    
    def detect_loop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False
    
    def remove_duplicates(self):
        prev = None
        dup_values = dict()
        temp = self.head
        while temp:
            if temp.data in dup_values:
                prev.next = temp.next
                temp = None
            else:
                dup_values[temp.data] = 1
                prev = temp
            temp = prev.next
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

def main():
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insert_after(llist.head.next, 8)
    print("Created linked list is: ", end="")
    llist.print_list()
    print("Element at index 3 is: ", llist.get_nth(3))
    print("Element at index 3 from last is: ", llist.get_nth_from_last(3))
    print("Middle element is: ", llist.get_middle())
    print("Count of nodes is: ", llist.count())
    print("List has loop: ", llist.detect_loop())
    llist.remove_duplicates()
    print("List after removing duplicates: ", end="")
    llist.print_list()
    llist.reverse()
    print("List after reversing: ", end="")
    llist.print_list()
    llist.delete_node(1)
    print("List after deleting node 1: ", end="")
    llist.print_list()
    llist.delete_node_at_position(2)
    print("List after deleting node at position 2: ", end="")
    llist.print_list()
    llist.delete_list()
    print("List after deleting entire list: ", end="")
    llist.print_list()

if __name__ == "__main__":
    main()
