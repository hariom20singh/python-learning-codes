class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
      self.headval = None
    #Traversing and printing the list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list1 = SLinkedList()
lis=[]
print("Enter 10 elements")
for i in range(10):
    a=int(input())
    lis.append(a);
list1.headval = Node(lis[0])
printval = list1.headval
for i in range(1,10):
    e=Node(lis[i])
    printval.nextval=e
    printval=printval.nextval
print("printed linked list is:")
list1.listprint()
