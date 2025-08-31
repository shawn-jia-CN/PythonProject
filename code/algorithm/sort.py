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
            insertIndex = orderedTail
            value = self.arr[orderedTail + 1]
            while insertIndex >= 0:
                if self.arr[insertIndex] > value:
                    self.arr[insertIndex + 1 ] = self.arr[insertIndex]
                else:
                    self.arr[insertIndex + 1 ] = value
                    break
                insertIndex = insertIndex - 1
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
    