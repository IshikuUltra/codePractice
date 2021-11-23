# Bubble sort algorithm
# Test it on DoubleLinkedList
# from dllTest import *

def bubble_sort(numbers): #-> numbers is test.begin
    #Dont overcomplicate the system.
    while True:
        lastNode = numbers
        curNode = numbers.next
        unSorted = True #assume list is sorted
        while curNode:
            if lastNode.data > curNode.data:
                lastNode.data, curNode.data = curNode.data, lastNode.data
                unSorted = False
            curNode, lastNode = curNode.next, lastNode.next
        if unSorted: break

    return numbers       


# dllInstance = test_push()
# print(bubble_sort(dllInstance)) 