# Bubble sort algorithm
# Test it on DoubleLinkedList
from dllTest import *

# After coding this, make the dll file actually dynamic...smh
# make it so calling node.last actually gets the entire last node

def bubble_sort(numbers): #-> numbers is test.begin
    #Dont overcomplicate the system.
    while True:
        lastNode = numbers
        curNode = numbers.next
        unSorted = True #assume list is sorted
        while curNode:
            if lastNode.data > curNode.data:
                lastNode.data, curNode.data = curNode.data, lastNode.data
                curNode.last = lastNode.data
                unSorted = False
            curNode, lastNode = curNode.next, lastNode.next
        if unSorted: break

    return numbers

            
            




# dllInstance = test_push()
# print(bubble_sort(dllInstance)) 