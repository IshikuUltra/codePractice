#tests for stack.py
from stack import *

def test_push():
    test = Stack()
    test.push(0)
    test.push(1)
    assert test.count() == 2
    print(test.count())
    test.push(2)
    test.pop() # pop is messing with my pionters
    test.push(4)
    assert test.count() == 3
    print(test.begin)

def test_dump(): #dump everything after mark
    test = Stack()
    test.push(0)
    test.push(1)
    test.push(2)
    test.push(3)
    test.dump(2)
    print(test.begin)

# test_push()
test_dump()