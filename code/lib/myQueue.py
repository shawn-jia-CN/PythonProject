from myErrorType import *
from myStack import ListNode

class myQueue:
    def __init__(self, capacity):
        self.capacity : int | 0 = capacity
        self.length : int | 0  = 0
        pass

    def enQueue(self, val):
        pass

    def deQueue(self) -> int:
        pass

    def toArr(self):
        pass

    def isEmpty(self):
        return self.length == 0
    
    def isFull(self):
        return self.length == self.capacity
    

class arrQueue(myQueue):
    def __init__(self, capacity: int, data: list[int]):
        super().__init__(capacity=capacity)
        self.tail = 0
        self.head = 0
        self.data = [0] * capacity 
        for d in data:
            self.enQueue(d)


    def enQueue(self, val):
        if self.isFull():
            return myRerunValue(returnCode=NoCapacity)
        self.data[self.tail] = val
        self.tail = self.getNextIndex(self.tail)
        self.length = self.length + 1
        return 
        
    def deQueue(self):
        if self.isEmpty():
            return myRerunValue(returnCode=IsEmpty)
        self.head = self.getNextIndex(self.head)
        self.length = self.length - 1

    def toArr(self):
        ret = []
        index = 0
        tmp = self.head
        while index < self.length:
            ret.append(self.data[tmp])
            tmp = self.getNextIndex(tmp)
            index = index + 1
        return ret
    
    def getNextIndex(self, index):
        return (index + 1) % self.capacity

class listQueue(myQueue):
    def __init__(self, capacity: int , data: list[int]):
        super().__init__(capacity)
        self.head : ListNode | None = None
        self.tail : ListNode | None = None
        for d in data:
            self.enQueue(d)

    def enQueue(self, val):
        if self.isFull():
            return myRerunValue(returnCode=NoCapacity)
        node = ListNode(val=val)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length = self.length + 1
        return 
    
    def deQueue(self):
        if self.isEmpty():
            return myRerunValue(returnCode=IsEmpty)
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length = self.length - 1
    
    def toArr(self):
        ret = []
        tmp = self.head
        while tmp is not None:
            ret.append(tmp.data)
            tmp = tmp.next
        return ret
    

class myQueueTool:
    def __init__(self):
        self.queue : myQueue | None = None
        pass

    def createQueue(self, data:list[int], capacity:int) -> myQueue:
        pass

    def doTest(self):
        tmp = [1, 2, 3]
        s = self.createQueue(tmp, 5)
        print(s.toArr())
        s.enQueue(4)
        print(s.toArr())
        s.enQueue(5)
        print(s.toArr())
        s.deQueue()
        print(s.toArr())
        s.enQueue(4)
        print(s.toArr())
        s.deQueue()
        print(s.toArr())

class myArrQueueTool(myQueueTool):
    def __init__(self):
        super().__init__()
    def createQueue(self, data, capacity) -> myQueue:
        return arrQueue(capacity=capacity, data=data)
    
class myListQueueTool(myQueueTool):
    def __init__(self):
        super().__init__()
    def createQueue(self, data, capacity) -> myQueue:
        return listQueue(capacity=capacity, data=data)

def run():
    t = myListQueueTool()
    t.doTest()

if __name__ == "__main__":
    run()




    

