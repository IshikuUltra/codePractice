# Stack data-strcuture

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        nval = self.data and self.next or None
        return f"{self.data}:{self.next}"


class Stack:
    def __init__(self):
        self.begin = None
        self.top = None

    def push(self,data):
        node = StackNode(data)
        if self.begin is None:
            self.top = node
            self.begin = node
        else:
            self.top.next = node
            self.top = node

# Incorrect pointers in pop() fix tomorrow
    def pop(self): # you need to move self.top back one also
        tmp = self.begin
        while tmp.next != None:
            if tmp.next.next is None:
                tmp.next = None
                self.top = tmp
                break
            tmp = tmp.next

    def tops(self):
        return self.top

    def count(self):
        counted = 0
        tmp = self.begin
        while tmp is not None:
            counted +=1
            tmp = tmp.next
        return counted
            

    def dump(self, mark):
        # debugging function that dumps the contents of the stack from mark
        tmp = self.begin
        while tmp.next != None:
            if tmp.data == mark:
                tmp.next = None
                self.top = tmp
                break
            tmp = tmp.next