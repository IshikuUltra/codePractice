##Merge sort algorithm

def count(numbers):
    count = 1
    while numbers.next:
        numbers = numbers.next
        count += 1
    return count

def merge_sort(numbers):
    sorted = merge_node(numbers)
    return sorted

def merge_node(start):
    if start.next == None: #'if start.next' is an statement
        return start # loads nodes into listLeft, listRight

    mid = count(start) // 2
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next

    mid_point = scanner.next

    scanner.next = None
    mid_point.last = None

    #sweet sweet recursion
    listLeft = merge_node(start)
    listRight = merge_node(mid_point)

    return merge(listLeft, listRight)


def merge(left, right):
    result = None

    if left is None: return right
    if right is None: return left
    
    if left.data < right.data:
        result = left
        result.next = merge(left.next, right) #
    else:
        result = right
        result.next = merge(left, right.next)

    result.next.last = result 
    return result #where is this being stored?