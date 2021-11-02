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
            self.begin = self.end #...
        else:
            self.end.next = curNode 
            self.end = curNode


list = LinkedList()
list.push(1)
list.push(2)
print(list.begin)
print(list.begin.next == None)