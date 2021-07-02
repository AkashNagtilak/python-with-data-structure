class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
        

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
        
    def listprint(self):
        printval = self.headval
        
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            

list1 = SLinkedList()
list1.headval = Node('Man')
e2 = Node('Tue')
e3 = Node('Thur')

list1.headval.nextval = e2
e2.nextval = e3
list1.Inbetween(list1.headval.nextval,"Fri")
list1.listprint()



        