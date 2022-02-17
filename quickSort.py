# Must be done Recursively

class QuickSort:
    def __init__(self):
        self.i = 0
        self.j= -2

    def partition(self, arr):
        pivot = arr[-1]
        length = (len(arr)//2)+1
        itemLeft, itemRight = arr[self.i], arr[self.j]
        if itemLeft > itemRight:
            tmpLeft, tmpRight = itemLeft, itemRight
            arr[self.i], arr[self.j] = tmpRight, tmpLeft
        if self.i == length:
            return self.sort(arr, length)
        print(arr)
        self.i=self.i+1
        self.j=self.j-1
        return self.partition(arr)

    def swap(self,arr):
        pass
    
    def sort(self, arr, length):
        leftList = arr[:length]
        rightList = arr[length:]
        print(leftList, rightList)
        return 0


QS = QuickSort()
arr = [8,7,3,2,1,5,9]
QS.partition(arr)
