# Bubble sort algorithm
# Test it on DoubleLinkedList
from dllTest import *

def bubble_sort(numbers): #-> numbers is test.begin
    while True:
        is_sorted = True
        curNode = numbers.next
        while True:
            if curNode.data < curNode.last.data:
                curNode.last.data, curNode.data = curNode.data, curNode.last.data
            curNode = curNode.next
            is_sorted = False
        if is_sorted: break

            
            




dllInstance = test_push()
print(bubble_sort(dllInstance)) 