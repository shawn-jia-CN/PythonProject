import lib.myErrorType

class mySearchAlgorithm:
    def __init__(self, input):
        self.arr = input
        self.arrLength = len(input)
        self.targetIndex = 0

    def binarySearch(self, target):
        left = 0
        right = self.arrLength - 1
        while left != right:
            mid = int((left + right) / 2)
            if self.arr[mid] == target:
                self.targetIndex = mid
                return self.success()
            elif self.arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if self.arr[left] == target:
            self.targetIndex = left
            return self.success()
        return self.failed()

    def success(self):
        return lib.myErrorType.myRerunValue(returnCode=lib.myErrorType.NoError)

    def failed(self):
        return lib.myErrorType.myRerunValue(returnCode=lib.myErrorType.NotFound)