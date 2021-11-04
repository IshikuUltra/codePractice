######################
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.last = None

    def __repr__(self): 
        nval = self.data and self.next or None
        pval = self.last and self.last or None #not complete
        return f"[D:{self.data}, P:{repr(pval)}, N:{repr(nval)}]"

class DoubleLinkedList: # no need for (object) in P3 

    def __init__(self):
        self.begin = None
        self.end = None
    
    def push(self,data):
        newNode = Node(data)
        if self.begin is None:
            self.begin = newNode
            self.end = self.begin
        else:
            self.end.next = newNode
            self.end.next.last = self.end.data # Seems legit
            self.end = newNode

    def pop(self): # remove last node
        pass
        # self.end = self.end.last
        # self.end.next = None

    def shift(self):
        pass

    def unshift(self):
        pass

    def detach_node(self, node): #removes node from anywhere in list
        pass

    def remove(self,obj):
        pass

    def first(self):
        pass

    def last(self):
        pass
