from testTest import *

def test_push():
    colors = LinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("ultramarine blue")
    assert colors.count() == 2

def test_pop():
    colors = LinkedList()
    colors.push("magenta")
    colors.push("Alizarin")
    return colors.pop()