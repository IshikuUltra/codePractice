#tests for stack.py
from stack import *

def test_push():
    test = Stack()
    test.push(0)
    print(id(test.begin))
    test.push(1)
    test.push(2)
    test.pop()
    test.push(4)

    print(id(test.begin))
    assert test.count() == 2
    # test.pop()
    # print(test.tops())
    print(test.begin)
    # test.push(3)
    # assert test.count() == 3
    # print(test.count())

test_push()