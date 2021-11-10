# pg 63 in Zed Shaws lmpthw -> implementation of queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        nval = self.data and self.next or None:
        return f"{self.data}:{self.next}"

class Queue:
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self,data):
        node = Node(data)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        else: 
            self.end.next = node
            self.end = node

    def pop(self):
        pass

    def top(self):
        pass

    def count(self):
        pass
