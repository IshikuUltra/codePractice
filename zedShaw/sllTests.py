##################################################################
from dll import *

def test_push():
    colors = DoubleLinkedList()
    colors.push(1)
    assert colors.count() == 1
    colors.push(2)
    colors.push(3)
    colors.pop()
    assert colors.count() == 2
    return colors.begin

def test_pop():
    colors = DoubleLinkedList()
    colors.push("magenta")
    colors.push("Alizarin")
    return colors.pop()

def test_shift():
    colors = DoubleLinkedList()
    colors.push(1)
    colors.push(2)
    colors.push(3)
    colors.shift(0) #if you use 0 it fucks it up? WTF
    colors.push(4)
    # return colors.begin

# print(test_push())
# print(test_pop())
print(test_shift())
