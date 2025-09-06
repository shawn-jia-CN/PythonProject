from lib.myDataStructure import myList
from  algorithm.sort import *
from algorithm.search import mySearchAlgorithm
from lib.myErrorType import *


def main():
    t=sortTool()
    test = myList(strIn="1,6,3, 5,7,2,3,100, 2000", sortTool=t)
    #test.printMyList()
    #sortListTool = mySortAlgorithm(input=test)
    #sortListTool.insertSort()
    #sortListTool.selectSort()
    test.printMyList()
    test.doSort()
    test.printMyList()
    """
    searchTool = mySearchAlgorithm(input=test)
    ans = searchTool.binarySearch(3)
    if ans.success() :
        print("index is {}".format(searchTool.targetIndex))
    else:
        print("error message = {}".format(ans.getErrorMsg()))
    """

    
if __name__ == "__main__":
    main()
