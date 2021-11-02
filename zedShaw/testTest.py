#####################################
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
            

    def count(self):
        temp = self.begin
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count


    def pop(self, thisNode=begin): 
        tmp = None
        if thisNode.next.next == None:
            tmp = thisNode.next.next
            thisNode.next = None
            return tmp
        else:
            return self.pop(thisNode.next)

    def unshift(self):
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
sll.push(9)
sll.push(10)
print(sll.count())
print(sll.pop())
# print(sll.pop()) # Something is severing self.begin from the node chain
print(sll.begin)

# sll.push(99)
# print(sll.begin)
# print(sll.pop())
