##Merge sort algorithm

def count(numbers):
    count = 1
    while numbers.next:
        numbers = numbers.next
        count += 1
    return count