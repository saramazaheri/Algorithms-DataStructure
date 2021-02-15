class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AddFirst(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def AddLast(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
    def RemoveFirst(self):
        self.head=self.head.next
    
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
        while first is not None or second is not None:
            sum_value = carry
            if first is not None:
                sum_value += int(first.data)
                first = first.next
            if second is not None:
                sum_value += int(second.data)
                second = second.next
            node = Node(sum_value % 10)
            carry = sum_value // 10
            if temp is None:
                temp = prev = node
            else:
                temp.next = node
                temp = temp.next
        if carry > 0:
            temp.next = Node(carry)
        return prev

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()

def findmax(x,y):
    for i in range(len(x)):
        if x[i]>y[i]:
            return('first')
        elif y[i]>x[i] :
            return('second')
    return('equal')

first = LinkedList()
second = LinkedList()

x=input("Enter Your First Number: ")
first = LinkedList()

for i in range(0,len(x)):
    if x[i] not in ('+','-'):
        first.AddFirst(x[i])
if x[0]=='-':
    first.AddFirst('-')
else:
    first.AddFirst('+')
firstsign=first.head.data

y=input("Enter Your Second Number: ")
second = LinkedList()

for i in range(0,len(y)):
    if y[i] not in ('+','-'):
        second.AddFirst(y[i])
if y[0]=='-':
    second.AddFirst('-')
else:
    second.AddFirst('+')
secondsign=second.head.data

resultlinkedlist=LinkedList()

if secondsign==firstsign:
    result=first.addTwoLists(first.head.next, second.head.next)
    while result is not None:
        resultlinkedlist.AddFirst(result.data)
        result=result.next
    resultlinkedlist.AddFirst(firstsign)
    
else:
    xsign=firstsign
    x=[i for i in x if i not in ('-','+')]
    x=''.join(x)
    ysign=secondsign
    y=[i for i in y if i not in ('-','+')]
    y=''.join(y)
    
    if len(x)>len(y):
        for i in range(len(x)-len(y)):
            second.AddLast('0')
        y=(len(x)-len(y))*'0'+y
        
    else:
        for i in range(len(y)-len(x)):
            first.AddLast('0')
        x=(len(y)-len(x))*'0'+x
    #print(x,y)

    if findmax(x,y)=='first':
        temp=second.head.next
        temp.data=str(10-int(temp.data))
        temp=temp.next
        while temp is not None:
            temp.data=str(9-int(temp.data))
            temp=temp.next
        result=first.addTwoLists(first.head.next, second.head.next)
        while result is not None:
            resultlinkedlist.AddFirst(result.data)
            result=result.next
        resultlinkedlist.RemoveFirst()  
        resultlinkedlist.AddFirst(firstsign)
    else:
        temp=first.head.next
        temp.data=str(10-int(temp.data))
        temp=temp.next
        while temp is not None:
            temp.data=str(9-int(temp.data))
            temp=temp.next
        result=first.addTwoLists(first.head.next, second.head.next)
        while result is not None:
            resultlinkedlist.AddFirst(result.data)
            result=result.next
        resultlinkedlist.RemoveFirst()  
        resultlinkedlist.AddFirst(secondsign)

# print("First List is ")
# first.printList()
# print ("Second List is ")
# second.printList()
resultlinkedlist.printList()