from myErrorType import *

class ListNode:
    def __init__(self, val: int):
        self.data : int = val
        self.next : ListNode | None = None


class myStack:
    def __init__(self):
        pass

    def pop(self):
        pass

    def push(self):
        pass

    def peek(self):
        pass

    def toArr(self):
        pass


class linkStack(myStack):
    def __init__(self, data: list[int], capacity: int):
        self.top : ListNode | None = None
        super().__init__()
        self.capacity = capacity
        self.size = 0
        for item in data:
            self.push(item)

        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def pop(self):
        if self.isEmpty():
            return myRerunValue(returnCode=IsEmpty)
        tmp = self.top
        self.top = self.top.next
        self.size = self.size - 1
        del tmp
        return 

    def peek(self) -> int:
        if self.isEmpty():
            return myRerunValue(returnCode=IsEmpty)
        return self.top.data
    
    def push(self, data: int):
        if self.isFull():
            return myRerunValue(returnCode=NoCapacity)
        tmp = ListNode(data)
        if self.top == None:
            self.top = tmp
        else:
            tmp.next = self.top
            self.top = tmp
        self.size = self.size + 1

    def toArr(self) -> list[int]:
        l = []
        tmp = self.top
        while (tmp) :
            l.append(tmp.data)
            tmp = tmp.next
        return l
    


class arrStack(myStack):
    def __init__(self, data: list[int], capacity: int):
        super().__init__()
        self.top : int | 0 = 0
        self.capacity = capacity
        self.size = 0
        self.arr : list[int] | None = [0] * (self.capacity + 1)
        for item in data:
            self.push(item)

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity

    def push(self, val : int):
        if self.isFull():
            return myRerunValue(returnCode=NoCapacity)
        self.arr[self.top] = val
        self.top = self.top + 1
        self.size = self.size + 1

    def peek(self) -> int:
        if self.isEmpty():
            return myRerunValue(returnCode=IsEmpty)
        return self.arr[self.top - 1]

    def pop(self):
        if self.isEmpty():
            return myRerunValue(returnCode=IsEmpty)
        self.top = self.top - 1
        self.size = self.size - 1

    def toArr(self) -> list[int]:
        l = []
        tmp = self.top - 1
        while tmp >= 0:
            l.append(self.arr[tmp])
            tmp  = tmp - 1
        return l 
        
class stackTool:
    def __init__(self):
        self.stack : myStack | None = None
        pass
    def createStack(self, data: list[int], capacity: int) -> myStack:
        pass

    def doTest(self):
        tmp = [1, 2, 3]
        s = self.createStack(tmp, 20)
        print(s.toArr())
        print(s.peek())
        s.push(4)
        print(s.toArr())
        s.push(5)
        print(s.toArr())
        s.pop()
        print(s.toArr())



class linkStackTool(stackTool):
    def __init__(self):
        super().__init__()
    
    def createStack(self, data, capacity):
        return linkStack(data, capacity)



class arrStackTool(stackTool):
    def __init__(self):
        super().__init__()
    
    def createStack(self, data, capacity):
        return arrStack(data, capacity)


def run():
    t = arrStackTool()
    t.doTest()



if __name__ == "__main__":
    run()






