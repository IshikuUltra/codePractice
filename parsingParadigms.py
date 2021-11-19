# https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
# Pass by reference vs pass by value vs PASS BY OBJECT REFERENCE

def reassign(list):
  list = [0, 1]

def append(list):
  list.append(1)

list = [0]
reassign(list)
append(list)