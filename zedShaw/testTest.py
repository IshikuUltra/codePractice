# # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Node:
 
    def __init__(self, data):
        self.data = data  
        self.next = None
        #adding another link would defeat the whole "single linked list" thing dont you think.....
    
    def __repr__(self):
        nval = self.next and self.next or None #its all in the formatting... change self.next -> self.next.data
        return f"[{self.data}:{repr(nval)}]" #__repr__ is just debugging format, you can call it on the node!


class LinkedList:

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, val):    
        curNode = Node(val)
        if self.begin is None: 
            self.end = curNode
            self.begin = self.end # how can i see the actual pointer to the object? 
        else:
            self.end.next = curNode # why is sll.end receiving the node but not self.begin (only after pop is invoked)
            self.end = curNode
            
    def count(self): # dont touch it perfect
        temp = self.begin
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def pop(self): # removes last item and returns it
        tmp = self.begin
        while tmp.next != None:
            if tmp.next.next == None:
                self.end = tmp
                tmp.next = None
                print(tmp)
                break
            tmp = tmp.next

    def shift(self, data): # insert node at beginning of list
        node = Node(data)
        tmp = self.begin
        node.next = tmp 
        self.begin = node

    def unshift(self): #removes first node from list
        tmp = self.begin
        self.begin = self.begin.next
        tmp = None
    
    def first(self): #returns first node
        return f"{self.begin.data}"

    def last(self): #returns last node
        return f"{self.end.data}"

    def get(self, index): #get node at certain index
        # idea: loop through the nodes mapping a index to their id()??
        curIndex = 0
        tmp = self.begin
        while curIndex != index+1:
            if curIndex == index:
                return f"{tmp.data}"
            tmp = tmp.next
            curIndex+=1

    def printList(self):
        print(self.begin)

sll = LinkedList()
sll.push(1)
sll.push(2)
sll.push(8)
sll.push(9)
sll.push(10)

# print(sll.count())
# print(sll.begin)
# print(sll.pop())
# print(sll.begin)
# sll.push(11)
# sll.unshift()
# print(sll.begin)

# sll.push(22)
# print(sll.begin)
# print(sll.first())

# print(sll.last())
# print(sll.get(4))
# print(sll.begin)
# sll.push(99)
# print(sll.begin)
# print(sll.pop())
sll.shift(100)
print(sll.begin)
