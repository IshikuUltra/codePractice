class Node: # no need for (object) in P3 

    def __init__(self,data):
        self.data = data
        self.next = None
        self.last = None

    def __repr__(self): 
        nval = self.data and self.next or None 
        pval = self.last and self.last.data or None 
        return f"[D:{self.data}, L:{repr(pval)}, N:{repr(self.next)}]"


class DoubleLinkedList: 

    def __init__(self):
        self.begin = None
        self.end = None
    
    def push(self, data):
        newNode = Node(data)
        if self.begin is None:
            self.begin = newNode
            self.end = self.begin
        else:
            self.end.next = newNode
            # WHY IS THE FOLLOWING LINE SMOKING MY LIST??
            self.end.next.last = self.end.data 
            self.end = newNode #

    def pop(self): # remove last node
        self.end = self.end.last
        self.end.next = None

    def count(self):
        tmp = self.begin
        count = 0
        while tmp != None:
            count += 1
            tmp = tmp.next
        return count

    def shift(self,data): #Trying to push 0 on this list disrupts its print
        newNode = Node(data)
        newNode.next = self.begin
        self.begin = newNode
        self.begin.next.last = self.begin.data
        return self.begin

    def unshift(self): #removes first item
        self.begin.next.last = None
        self.begin = self.begin.next


    def detach_node(self, node): #removes node from anywhere in list
        tmp = self.begin
        while tmp.next is not None:
            if tmp.data == node:
                tmp.last.next = tmp.next
                return self.begin
            tmp = tmp.next

    def first(self): 
        return self.begin

    def last(self): 
        return self.end
