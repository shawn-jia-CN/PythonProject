from lib.myDataStructure import myList
from  algorithm.sort import mySortAlgorithm
from algorithm.search import mySearchAlgorithm
from lib.myErrorType import *


def main():
    test = myList(strIn="1,6,3, 5,7,2,3,100, 2000")
    test.printMyList()
    sortListTool = mySortAlgorithm(input=test)
    #sortListTool.insertSort()
    sortListTool.selectSort()
    print(test)
    searchTool = mySearchAlgorithm(input=test)
    ans = searchTool.binarySearch(3)
    if ans.success() :
        print("index is {}".format(searchTool.targetIndex))
    else:
        print("error message = {}".format(ans.getErrorMsg()))

    
if __name__ == "__main__":
    main()
