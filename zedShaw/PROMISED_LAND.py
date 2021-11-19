class Node:
 
    def __init__(self, data):
        self.data = data  
        self.next = None  
    
    def __repr__(self):
        nval = self.next and self.next or None #its all in the formatting... change self.next -> self.next.data
        return f"[{self.data}:{repr(nval)}]"

##################################
# self.begin was never equal to self.end... it only referenced the same Node object...
##################################

A = Node(0) # NODE INSTANCE 1
# print(id(A))
B = A
A.next = Node("New")
# print(id(A))
A.next = Node("Anotha One")
# print(id(A))
print(B)

A = Node("Who") # NODE INSTANCE 2
# print(id(A))
A.next = Node("Anotha One")
print(B)