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

class sortTool:
    def __init__(self):
        pass

    def sort(self, input):
        t = mySortAlgorithm(input)
        t.selectSort()


class mergeSortTool:
    def __init__(self):
        pass

    def merge(self, left ,right):
        ans = []
        leftIndex = 0
        rightIndex = 0
        leftLen = len(left)
        rightLen = len(right)
        while(leftIndex < leftLen or rightIndex < rightLen):
            if leftIndex == leftLen:
                ans.append(right[rightIndex])
                rightIndex = rightIndex + 1
            elif rightIndex == rightLen:
                ans.append(left[leftIndex])
                leftIndex = leftIndex + 1
            else:
                if left[leftIndex] < right[rightIndex]:
                    ans.append(left[leftIndex])
                    leftIndex = leftIndex + 1
                else:
                    ans.append(right[rightIndex])
                    rightIndex = rightIndex + 1
        return ans

    def sort(self, input):
        tmp = input.arr[: len(input)]
        ans = self.doInternalSort(tmp)
        for i in range(len(ans)):
            input[i] = ans[i]

    def doInternalSort(self, input):
        if len(input) <= 1:
            return input
        mid = len(input) // 2
        return self.merge(self.doInternalSort(input[: mid]),  self.doInternalSort(input[mid: len(input)]))
    



class qSortTool:
    def __init__(self):
        pass

    def sort(self, input):
        tmp = input.arr[: len(input)]
        ans = self.doInternalSort(tmp)
        for i in range(len(ans)):
            input[i] = ans[i]


    def doInternalSort(self, input):
        if len(input) <= 1:
            return input
        pivot = input[0]
        left = []
        right = []
        index = 1
        while index < len(input):
            if input[index] < pivot:
                left.append(input[index])
            else:
                right.append(input[index])
            index = index + 1
        return self.doInternalSort(left) + [pivot] + self.doInternalSort(right)