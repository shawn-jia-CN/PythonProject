"""
寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
"""


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merge = []
    index1 = 0
    index2 = 0 
    print(nums1)
    print(nums2)
    while (index1 < len(nums1) or index2 < len(nums2)):
        if (index1 < len(nums1) and index2 < len(nums2)):
            if nums1[index1] < nums2[index2]:
                merge.append(nums1[index1])
                index1 = index1 + 1
            else:
                merge.append(nums2[index2])
                index2 = index2 + 1      
        elif index1 < len(nums1):
            merge.append(nums1[index1])
            index1 = index1 + 1   
        else:
            merge.append(nums2[index2])
            index2 = index2 + 1   
    
    mid = len(merge)//2
    if len(merge) % 2 == 0:
        return float(merge[mid - 1] + merge[mid])/ 2
    else:             
        return float((merge[mid]))

def run():
   # nums = [2,7,11,15], target = 9
    input1 = [1, 2]
    input2 = [3]
    print("ans = {}".format(findMedianSortedArrays(input1, input2)))
    return 

if __name__ == "__main__":
    run()
        