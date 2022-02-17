import bubble_sort
import mergeSort
import quickSort
from dll import *
from random import randint

def random_list(size):
    test = DoubleLinkedList()
    n=0
    while n != size:
        test.push(randint(1,50))
        n +=1
    # print(test.begin)
    return test.begin

def is_sorted(num_list):
    while num_list is not None:
        if num_list.data > num_list.next.data:
            return False
        num_list = num_list.next
        return "SORTED"

def test_bubble_sort():
    numbers = random_list(3)

# print(test_bubble_sort())
# print(is_sorted(test_bubble_sort()))

def test_merge_sort():
    numbers = random_list(4)
    print(numbers)
    sorted = mergeSort.merge_sort(numbers)
    return sorted

# print(test_merge_sort())
# print(test_merge_sort())
# print(is_sorted(test_merge_sort))

def quick_sort():
    numbers = random_list(4)
    sorted = quickSort.lowToHight(numbers)
    return sorted

print(quick_sort())
