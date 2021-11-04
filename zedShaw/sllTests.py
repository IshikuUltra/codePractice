##################################################################
from dll import *

def test_push():
    colors = DoubleLinkedList()
    colors.push(1)
    # assert colors.count() == 1
    colors.push(2)
    colors.push(3)
    # colors.pop()
    # assert colors.count() == 2
    return colors.begin

# def test_pop():
#     colors = DoubleLinkedList()
#     colors.push("magenta")
#     colors.push("Alizarin")
#     return colors.pop()

print(test_push())