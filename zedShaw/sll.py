
class SingleLinkedListNode(object):

    def __init__(self,value,nxt):
        self.value=value
        self.nxt=nxt

    def __repr__(self):
        nval = self.nxt and self.nxt.value or None
        return f"[{self.value}:{repr(nval)}]" #__repr__ is just debugging format, you can call it on the node!


class SingleLinkedList(object):
    
    def __init__(self):
        self.begin=None
        self.end=None

    def push(self,value):
        sll = SingleLinkedListNode(value, None)
        
        if self.begin == None: 
            self.end = sll
            self.begin = self.end
        else:
            self.end.nxt = sll
            self.end = sll


SLL = SingleLinkedList()
SLL.push(0)
SLL.push(1)
SLL.push(2)
SLL.push(3)
SLL.push(4)

print(SLL.begin)
print(SLL.end)