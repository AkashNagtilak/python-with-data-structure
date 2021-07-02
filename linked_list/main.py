class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
        
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

#link First Node to 2nd Node
list1.headval.nextval = e2
#link 2nd node to 3rd node
e2.nextval = e3

