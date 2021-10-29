
class Node():

    def __init__(self, data):
        self.data = data
        self.nxt = None
    
    def __repr__(self): #repr formats the return object as a string. 
        nval = self.nxt and self.nxt or None #its all in the formatting... change self.next -> self.next.data
        return f"[{self.data}:{repr(nval)}]"


class Obj():
    def __init__(self):
        self.begin = None
        self.end = None
    
    def objPipeline(self, data):
        obj = Node(data)
        if self.begin == None:
            self.end = obj # VARIABLES CAN POINT AT MULTIPLE VALUES?????????????????????????????????????????????????????
            self.begin = self.end #what is actually happening here?
            # print(id(self.begin))
        else:
            self.end.nxt = obj #this is why the recursion error happens? this must be first because: 
            self.end = obj

        # print(id(self.end))
        # print(id(self.begin))
        # print(f" self.end.nxt {id(self.end.nxt)}")
        # print(f" self.begin.nxt {id(self.begin.nxt)}")

pipeline = Obj()
pipeline.objPipeline(0)
pipeline.objPipeline(1)
pipeline.objPipeline(2)

print(pipeline.begin)
print(pipeline.end)