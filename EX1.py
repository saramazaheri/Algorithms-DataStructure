#برنامه ای بنویسید که لیست تک پیوندی از اعداد 1 تا 10 را تشکیل داده و چاپ کند و سپس برعکس آن را چاپ کند.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
 
    def reverseUtil(self, k, prev):
        if k.next is None:
            self.head = k
            k.next = prev
            return
        next = k.next
        k.next = prev

        self.reverseUtil(next, k)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

liste = SLinkedList()

for i in range (1,11):
    liste.push(i)
 
print("Given linked list:")
liste.printList()
 
liste.reverse()

print("Reverse linked list:")
liste.printList()