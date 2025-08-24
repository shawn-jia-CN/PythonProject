class mySortAlgorithm:
    def __init__(self, input):
        self.arr = input
        self.length = len(self.arr)
        
    def swap(self, left , right):
        tmp = self.arr[left]
        self.arr[left] = self.arr[right]
        self.arr[right] = tmp

    def insertSort(self):
        orderedTail = 0
        while orderedTail < self.length - 1:
            tmpIndex = orderedTail + 1
            value = self.arr[tmpIndex]
            insertIndex = tmpIndex
            for index in range(orderedTail):
                if self.arr[index] > self.arr[tmpIndex]:
                    insertIndex = index
                    break
            if insertIndex != tmpIndex:
                #Need insert
                i = tmpIndex
                while i > insertIndex:
                    self.arr[i] = self.arr[i - 1]
                    i = i - 1
                self.arr[insertIndex] = value
            orderedTail = orderedTail + 1

    def selectSort(self):
        index = self.length
        while index > 0:
            maxIndex = 0
            for i in range(0, index):
                if self.arr[i] > self.arr[maxIndex]:
                    maxIndex = i
            self.swap(maxIndex, index - 1)
            index  = index - 1
    