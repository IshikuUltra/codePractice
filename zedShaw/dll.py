#########################################################################################
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
            self.end.next.last = self.end
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

    def unshift(self): #removes first item
        tmp = self.begin 
        self.begin = self.begin.next

#######
#Notes: 
    #1) node1.last wont point to node0.data
    #2) when calling detatch node every node.last after the detatched node dont dynamically update
######

    def detach_node(self, node): #removes node from anywhere in list
        tmp = self.begin
        while tmp:
            if tmp.data == node:
                tmp.last.next = tmp.next
                return tmp
            tmp = tmp.next

    def first(self): 
        return self.begin

    def last(self): 
        return self.end


test = DoubleLinkedList()
test.push(1)
test.push(2)
test.push(3)
test.shift(100) #shift(0) causes print to fall apart -> solved, its because of your'e nval setup -> 0 is None of some sorts in python
test.push(4)
# test.unshift()
test.detach_node(0)
# print(test.last())
print(test.begin) #when shifting 0, self.begin prints-> [D:0, L:None, N:None] -> solved 
# print(test.begin.next)#shfting 0 does still contain a pointer to node chain
