class Queue:
    def __init__(Self):
        Self.queue = list()
        
    def add(Self,dataval):
        if dataval not in Self.queue:
            Self.queue.insert(0,dataval)
            return True
            
        return False
        
    def remove(Self):
        if len(Self.queue)>0:
            return Self.queue.pop()
        return ("No element in queue")
    
    
TheQueue = Queue()
TheQueue.add(10)
TheQueue.add(20)

print(TheQueue.remove)
            
            