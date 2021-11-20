import bubble_sort
from dll import *
from random import randint

def random_list(size):
    test = DoubleLinkedList()
    n=0
    while n != size:
        test.push(randint(0,1000))
        n +=1
    return test.begin

def is_sorted(num_list):
    while num_list is not None:
        if num_list.data > num_list.next.data:
            return False
        num_list = num_list.next
        return "SORTED"

def test_bubble_sort():
    numbers = random_list(30)
    sorted = bubble_sort.bubble_sort(numbers)
    return sorted

print(test_bubble_sort())
print(is_sorted(test_bubble_sort()))

def test_merge_sort():
    pass
