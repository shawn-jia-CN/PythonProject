import lib.myErrorType as myErrorType
'''
    List structure
'''

CAPACITY = 100


class myList:
    def __init__(self, cap = CAPACITY, strIn = ""):
        self.__cap__ = cap
        self.__len__ = 0
        self.arr = [0] * self.__cap__
        if strIn != "":
            self.initWithStr(strIn)


    def __len__(self):
        return self.__len__
    
    def __getitem__(self, index):
        if index > self.__len__ or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        return self.arr[index]

    def __setitem__(self,index, value):
        if index > self.__len__ or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        self.arr[index] = value

    def __repr__(self):
        return self.toString()

    def initWithStr(self, strIn):
        if strIn != "":
            tmp = str(strIn).split(",")
            for elem in tmp:
                self.arr[self.__len__ ] = int(elem)
                self.__len__ = self.__len__ + 1
        return


    def getLength(self):
        return self.__len__
    
    def getCapacity(self):
        return self.__cap__
    
    def toString(self):
        ans = "["
        for i in range(self.getLength()):
            ans = ans + " " + str(self.arr[i])
        ans = ans + " ]"
        return ans

    def isFull(self):
        return self.__len__ == self.__cap__
    
    def isEmpty(self):
        return (self.__len__ == 0)

    def extend(self, cap):
        if cap <= self.__cap__:
            return self.errorMsg(myErrorType.InvaildParameter)
        newarr = [0] * cap
        for i in range(self.__len__):
            newarr[i] = self.arr[i]
        del self.arr
        self.arr = newarr
        self.__cap__ = cap

    def insert(self, index, value):
        if index > self.__len__ or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        if self.isFull():
            return self.errorMsg(myErrorType.NoCapacity)

        tail = self.__len__ + 1
        while tail > index:
            self.arr[tail] = self.arr[tail - 1]
            tail = tail - 1
        self.arr[index] = value
        self.__len__ = self.__len__ + 1
        return self.errorMsg(myErrorType.NoError)
    
    def remove(self, index):
        if index > self.__len__ or index < 0:
            return self.errorMsg(myErrorType.InvaildParameter)
        if self.isEmpty():
            return self.errorMsg(myErrorType.InvaildParameter)
        
        head = index
        while index < self.__len__:
            self.arr[index] = self.arr[index + 1]
            index = index + 1
        self.arr[self.__len__] = 0
        self.__len__ = self.__len__ -1 

        return 

    def append(self, value):
        self.insert(self.__len__, value)
        return 
    
    def pop(self):
        self.remove(self.__len__ - 1)
        return
    
    def printMyList(self):
        print("list - {0}, len - {1}, cap = {2}".format(self.toString(), self.getLength(), self.getCapacity()))
    
    def errorMsg(self, code):
        return myErrorType.myRerunValue(returnCode=code)
        

