import lib.myErrorType as myErrorType
'''
    List structure
'''

CAPACITY = 100


class myList:
    def __init__(self, cap = CAPACITY, strIn = "", sortTool = None):
        self.__cap__ = cap
        self.len = 0
        self.arr = [0] * self.__cap__
        self.sortTool = sortTool
        if strIn != "":
            self.initWithStr(strIn)


    def __len__(self):
        return self.len
    
    def __getitem__(self, index):
        if index > self.len or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        return self.arr[index]

    def __setitem__(self,index, value):
        if index > self.len or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        self.arr[index] = value

    def __repr__(self):
        return self.toString()

    def initWithStr(self, strIn):
        if strIn != "":
            tmp = str(strIn).split(",")
            for elem in tmp:
                self.arr[self.len ] = int(elem)
                self.len = self.len + 1
        return


    def getLength(self):
        return self.len
    
    def getCapacity(self):
        return self.__cap__
    
    def toString(self):
        ans = "["
        for i in range(self.getLength()):
            ans = ans + " " + str(self.arr[i])
        ans = ans + " ]"
        return ans

    def isFull(self):
        return self.len == self.__cap__
    
    def isEmpty(self):
        return (self.len == 0)

    def extend(self, cap):
        if cap <= self.__cap__:
            return self.errorMsg(myErrorType.InvaildParameter)
        newarr = [0] * cap
        for i in range(self.len):
            newarr[i] = self.arr[i]
        del self.arr
        self.arr = newarr
        self.__cap__ = cap

    def insert(self, index, value):
        if index > self.len or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        if self.isFull():
            return self.errorMsg(myErrorType.NoCapacity)

        tail = self.len + 1
        while tail > index:
            self.arr[tail] = self.arr[tail - 1]
            tail = tail - 1
        self.arr[index] = value
        self.len = self.len + 1
        return self.errorMsg(myErrorType.NoError)
    
    def remove(self, index):
        if index > self.len or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        if self.isEmpty():
            return self.errorMsg(myErrorType.InvaildParameter)
        
        head = index
        while index < self.len:
            self.arr[index] = self.arr[index + 1]
            index = index + 1
        self.arr[self.len] = 0
        self.len = self.len -1 

        return 

    def append(self, value):
        self.insert(self.len, value)
        return 
    
    def pop(self):
        self.remove(self.len - 1)
        return
    
    def printMyList(self):
        print("list - {0}, len - {1}, cap = {2}".format(self.toString(), self.getLength(), self.getCapacity()))
    
    def errorMsg(self, code):
        return myErrorType.myRerunValue(returnCode=code)
        
    
    def doSort(self):
        self.sortTool.sort(self)

