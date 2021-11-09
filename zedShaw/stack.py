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
        self.top = None

    def push(self,data):
        node = StackNode(data)
        if self.top is None:
            self.top = node
        else:
            self.top.next = node

    def pop(self):
        pass

    def top(self):
        pass

    def count(self):
        pass

    def dump(self, mark="----"):
        # debugging function that dumps the contents of the stack
        pass