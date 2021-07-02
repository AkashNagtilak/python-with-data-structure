class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
        
    def AddEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
            
        laste.nextval = NewNode
        
        
        
    def listprint(self):
        printval = self.headval
        
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
        
        
list1 = SLinkedList()
list1.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wen')

list1.headval.nextval = e2
e2.nextval = e3
list1.AddEnd('Sun')
list1.listprint()        