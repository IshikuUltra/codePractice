class Node:
 
    def __init__(self, data):
        self.data = data  
        self.next = None  
    
    def __repr__(self):
        nval = self.next and self.next or None #its all in the formatting... change self.next -> self.next.data
        return f"[{self.data}:{repr(nval)}]" #__repr__ is just debugging format, you can call it on the node!


class LinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, val):    #Note: the memory addr of self.begin stays the same but self.end changes
        curNode = Node(val)
        if self.begin is None: 
            self.end = curNode
            self.begin = self.end #This points to the first instance of curNode for life of program "pass-by-object reference"
        else:
            self.end.next = curNode # 
            self.end = curNode

    def count(self):
        counter = 0
        while self.begin != None:
            counter += 1
            self.begin = self.begin.next
        return counter

    def pop(self): #Clearing self.end might effect the push method
        pass

    def unshift(self):
        #remove first node
        pass
    
    def first(self):
        #returns first node
        pass

    def last(self):
        #returns last node
        pass

    def get(self):
        #get node at certain index
        pass

    def printList(self):
        print(self.begin)

sll = LinkedList()
sll.push(1)
sll.push(2)
sll.push(8)
# print(sll.pop())
print(sll.begin[1])
