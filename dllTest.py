from dll import *

def test_push():
    test = DoubleLinkedList()
    test.push(44)
    test.push(22)
    test.push(3)
    test.push(1)
    test.push(2)
    test.push(9)
    # print(test.begin)  
    # test.unshift()  
    # test.shift(666)
    return test.begin

# print(test_push())