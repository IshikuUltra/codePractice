# Bubble sort algorithm
# Test it on DoubleLinkedList
from dllTest import *

def bubble_sort(numbers): #-> numbers is test.begin
    while True:
        curNode = numbers
        if curNode.data > curNode.next.data:
            break
            




dllInstance = test_push()
print(bubble_sort(dllInstance)) 